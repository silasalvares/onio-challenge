import marshmallow as msh

class NewSellingSchema(msh.Schema):
    client_cpf = msh.fields.Str()
    value = msh.fields.Decimal()

class SellingSchema(msh.Schema):
    id = msh.fields.Str()
    client_cpf = msh.fields.Str()
    value = msh.fields.Decimal()
    date = msh.fields.DateTime()