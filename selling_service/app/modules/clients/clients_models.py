import mongoengine as me
from decimal import Decimal

class Client(me.Document):
    cpf = me.StringField(required=True)
    name = me.StringField()
    loyality_balance = me.DecimalField(required=True, default=Decimal('0'))
