from app.modules.clients import clients_service
from .selling_models import Selling

def register_selling(selling_data):
    client = clients_service.get_client(selling_data.get('client_cpf'))  
    return Selling(client=client, value=selling_data.get('value')).save()