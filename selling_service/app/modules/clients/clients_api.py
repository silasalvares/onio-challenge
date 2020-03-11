from flask import Blueprint, request
from app.utils.rest import JsonResponse, validate_schema
from app.modules.clients import clients_service
from app.modules.clients.clients_schemas import NewClientSchema, ClientSchema

clients = Blueprint('clients', __name__, url_prefix='/clients')

@clients.route('/', methods=['POST'])
@validate_schema(NewClientSchema())
def create_client(schema_data):
    new_client = clients_service.new_client(schema_data)
    return JsonResponse(data=ClientSchema().dump(new_client)).jsonify()

@clients.route('/', methods=['GET'])
def get_client_data():
    client_cpf = request.args.get('cpf')
    client_data = clients_service.get_client(client_cpf)
    return JsonResponse(data=ClientSchema().dump(client_data)).jsonify()