import mongoengine as me

class Client(me.Document):
    cpf = me.StringField()
    name = me.StringField()
