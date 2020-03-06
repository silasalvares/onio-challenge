from datetime import datetime
from decimal import Decimal

from app.utils.exeptions import InsuficientBalance
from .loyality_models import User, Entry

def register_user(user_data):
    return User(**user_data).save()

def credit(credit_data):
    user = User.objects(cpf=credit_data.get('cpf')).get()
    entry = Entry(
        date=datetime.now(),
        user=user,
        value=Decimal(credit_data.get('value'))
    ).save()

    user.balance += Decimal(entry.value)
    return user.save()

def debt(debt_data):
    user = User.objects(cpf=debt_data.get('cpf')).get()
    if (user.balance - Decimal(debt_data.get('value'))) < 0:
        raise InsuficientBalance

    entry = Entry(
        date=datetime.now(),
        user=user,
        value=Decimal(debt_data.get('value'))
    ).save()

    user.balance -= Decimal(entry.value)
    return user.save()

def get_score(user_cpf):
    return User.objects(cpf=user_cpf).get()