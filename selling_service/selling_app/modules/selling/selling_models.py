import mongoengine as me

class Sell():
    date = me.StringField(required=True)
    value = me.DecimalField(required=True)
    #client = me.ReferenceField('Client')
