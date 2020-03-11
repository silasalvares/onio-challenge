import simplejson
import marshmallow as msh

class NewClientSchema(msh.Schema):
    cpf = msh.fields.Str()
    name = msh.fields.Str()

class ClientSchema(msh.Schema):
    id = msh.fields.Str()
    cpf = msh.fields.Str()
    name = msh.fields.Str()
    loyality_balance = msh.fields.Decimal()

    class Meta:
        json_module = simplejson