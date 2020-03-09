import mongoengine as me
from datetime import datetime

class Selling(me.Document):
    client = me.ReferenceField('Client', required=True)
    value = me.DecimalField(required=True)
    date = me.DateTimeField(required=True, default=datetime.now())
    