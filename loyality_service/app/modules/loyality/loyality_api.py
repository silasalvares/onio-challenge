from flask import Blueprint, request

from app.utils.rest import JsonResponse, validate_schema
from app.modules.loyality.loyality_schemas import NewEntrySchema, EntrySchema, UserSchema
from app.modules.loyality import loyality_service

loyality = Blueprint('loyality', __name__, url_prefix='/')

@loyality.route('/', methods=['POST'])
@validate_schema(NewEntrySchema())
def credit(schema_data):
    entry_data = loyality_service.credit(schema_data)
    return JsonResponse(data=EntrySchema().dump(entry_data)).jsonify()

@loyality.route('/', methods=['GET'])
def get_balance():
    cpf = request.args.get('cpf')
    user_data = loyality_service.get_score(cpf)
    if (user_data is not None):
        return JsonResponse(data=UserSchema().dump(user)).jsonify()
    else:
        return JsonResponse(success=False, message='Usuário não encontrado').jsonify()