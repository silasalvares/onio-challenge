import mongoengine as me
from enum import Enum
from decimal import Decimal


class User(me.Document):
    cpf = me.StringField(required=True, unique=True)
    balance = me.DecimalField(required=True, default=Decimal(0))

class Entry(me.Document):
    date = me.DateTimeField(required=True)
    value = me.DecimalField(required=True)
    user = me.ReferenceField(User)
