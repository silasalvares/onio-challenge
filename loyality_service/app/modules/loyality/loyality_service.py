from datetime import datetime
from decimal import Decimal
from mongoengine.errors import DoesNotExist

from app.utils.exeptions import InsuficientBalance
from .loyality_models import User, Entry

def register_user(cpf):
    return User(cpf=cpf).save()

def credit(credit_data):
    user = None
    try:
        user = User.objects(cpf=credit_data.get('cpf')).get()
    except DoesNotExist:
        user = register_user(credit_data.get('cpf'))

    user.balance += Decimal(credit_data.get('value'))
    user.save()

    entry = Entry(
        date=datetime.now(),
        user=user,
        value=Decimal(credit_data.get('value'))
    ).save()

    return entry

def debt(debt_data):
    user = User.objects(cpf=debt_data.get('cpf')).get()
    if (user.balance - Decimal(debt_data.get('value'))) < 0:
        raise InsuficientBalance

    user.balance -= Decimal(debt_data.get('value'))

    entry = Entry(
        date=datetime.now(),
        user=user,
        value=Decimal()
    ).save()
   
    return entry

def get_score(user_cpf):
    try:
        return User.objects(cpf=user_cpf).get()
    except:
        return None