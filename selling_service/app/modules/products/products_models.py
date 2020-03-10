import mongoengine as me

class Product(me.Document):
    name = me.StringField(required=True)
    description = me.StringField()
    price = me.DecimalField(default=0.0)