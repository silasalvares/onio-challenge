import mongoengine as me
from enum import Enum
from decimal import Decimal


class User(me.Document):
    cpf = me.StringField(required=True)
    name = me.StringField(required=True)
    balance = me.DecimalField(required=True, default=Decimal(0))


# class EntryType(Enum):
#     D = 'Débito'
#     C = 'Crédito'

class Entry(me.Document):
    #entry_type = eme.StringEnumField(EntryTypeEnum, required=True)
    date = me.DateTimeField(required=True)
    value = me.DecimalField(required=True)
    user = me.ReferenceField(User)
