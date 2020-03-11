from flask import Blueprint

from app.utils.rest import JsonResponse, validate_schema
from app.modules.selling.selling_schemas import NewSellingSchema, SellingSchema
from app.modules.selling import selling_service

selling = Blueprint('selling', __name__, url_prefix='/selling')

@selling.route('/', methods=['POST'])
@validate_schema(NewSellingSchema())
def register_selling(schema_data):
    selling_data = selling_service.register_selling(schema_data)
    return JsonResponse(data=SellingSchema().dump(selling_data)).jsonify()