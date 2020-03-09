from .clients_models import Client

def new_client(client_data):
    return Client(**client_data).save()

def get_client(client_cpf):
    return Client.objects(cpf=client_cpf).get()