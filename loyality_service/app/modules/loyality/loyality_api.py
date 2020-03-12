from flask import Blueprint

from app.utils.rest import JsonResponse, validate_schema
from app.modules.loyality.loyality_schemas import NewEntrySchema, EntrySchema
from app.modules.loyality import loyality_service

loyality = Blueprint('loyality', __name__, url_prefix='/')

@loyality.route('/', methods=['POST'])
@validate_schema(NewEntrySchema())
def credit(schema_data):
    entry_data = loyality_service.credit(schema_data)
    print(entry_data)
    return JsonResponse(data=EntrySchema().dump(entry_data)).jsonify()