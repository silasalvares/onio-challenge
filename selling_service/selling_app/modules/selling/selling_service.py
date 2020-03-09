from .selling_models import Selling

def register_selling(selling_data):
    return Selling(**selling_data).save()