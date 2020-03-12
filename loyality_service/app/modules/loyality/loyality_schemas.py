import marshmallow as msh

class UserSchema(msh.Schema):
    cpf = msh.fields.Str()
    balance = msh.fields.Decimal()

class NewEntrySchema(msh.Schema):
    cpf = msh.fields.String()
    value = msh.fields.Decimal()

class EntrySchema(msh.Schema):
    user = msh.fields.Nested(UserSchema)
    date = msh.fields.DateTime()
    value = msh.fields.Decimal()