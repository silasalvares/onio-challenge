import simplejson
import marshmallow as msh

class NewProductSchema(msh.Schema):
    name = msh.fields.Str()
    description = msh.fields.Str()
    price = msh.fields.Decimal(places=2)

class ProductSchema(msh.Schema):
    id = msh.fields.Str()
    name = msh.fields.Str()
    description = msh.fields.Str()
    price = msh.fields.Decimal(places=2)

    class Meta:
        json_module = simplejson