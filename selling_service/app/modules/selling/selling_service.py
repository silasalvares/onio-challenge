from app.utils.events import emit_user_loyality_credit
from app.modules.clients import clients_service
from .selling_models import Selling

def register_selling(selling_data):
    client = clients_service.get_client(selling_data.get('client_cpf'))  
    if not client:
        client = clients_service.new_client({'cpf':selling_data.get('client_cpf')})
    selling = Selling(client=client, value=selling_data.get('value')).save()
    emit_user_loyality_credit(selling)
    return selling