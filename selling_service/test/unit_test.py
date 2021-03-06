import pytest
from bson import ObjectId
from decimal import Decimal
from mongoengine import connect, disconnect

from app.modules.products import products_service
from app.modules.clients import clients_service
from app.modules.selling import selling_service

connect('mongoenginetest', host='mongomock://localhost')

def test_when_new_product__id_is_set():
    product_data = {'name': 'Product 1', 'description': 'First Product', 'price': 10.0}
    new_product = products_service.create_product(product_data)
    assert type(new_product.id) == ObjectId

def test_when_new_client__id_is_set():
    client_data = {'cpf': '00000000191', 'name': 'First Client'}
    new_client = clients_service.new_client(client_data)
    assert type(new_client.id) == ObjectId
 
def test_when_client_requested__data_are_returned():
    client = clients_service.get_client('00000000191')
    assert client.name == 'First Client'
    assert type(client.id) == ObjectId
    assert client.loyality_balance == Decimal('0')

def test_when_new_selling__data_are_returned():
    selling_data = {'client_cpf': '00000000191', 'value': 10.0}
    new_selling = selling_service.register_selling(selling_data)
    assert type(new_selling.id) == ObjectId
    assert new_selling.client.name == 'First Client'
    assert new_selling.value == Decimal('10')

