import pytest
from decimal import Decimal
from mongoengine import connect

from app import app

connect('mongoenginetest', host='mongomock://localhost')

@pytest.fixture
def client():
    return app.test_client()

def test_when_new_product__data_are_stored(client):
    response = client.post('/products/', json={
        'name': 'Product 1', 
        'description': 'Fisrt Product',
        'price': 10.0
    })

    assert response.status_code == 200
    new_product = response.json.get('data')
    assert type(new_product['id']) == str
    assert new_product['name'] == 'Product 1'

def test_when_new_client__data_is_stored(client):
    response = client.post('/clients/', json={
        'cpf': '02547265508', 
        'name': 'New Client'
    })

    assert response.status_code == 200
    new_client = response.json.get('data')
    assert type(new_client['id']) == str
    assert new_client['cpf'] == '02547265508'

def test_client_details_requested__data_are_returned(client):
    response = client.get('/clients/?cpf=02547265508')

    assert response.status_code == 200
    client_data = response.json.get('data')
    assert type(client_data['id']) == str
    assert client_data['cpf'] == '02547265508'
    assert client_data['loyality_balance'] == Decimal('0')

def test_when_new_selling__data_is_returned(client):
    response = client.post('/selling/', json={
        'client_cpf': '02547265508',
        'value': 10.0
    })

    assert response.status_code == 200
    selling_data = response.json.get('data')
    assert type(selling_data['id']) == str
    assert selling_data['value'] == Decimal('10')

def test_when_new_selling__loyality_balance_is_updated(client):
    response = client.post('/clients/', json={
        'cpf': '01483535509',
        'name': 'Second Client'
    })
    assert response.status_code == 200
    client_data = response.json.get('data')
    assert client_data['loyality_balance'] == Decimal('0')
    
    response = client.post('/selling/', json={
        'client_cpf': '01483535509',
        'value': 10.0
    })

    assert response.status_code == 200

    response = client.get('/clients/?cpf=01483535509')
    assert response.status_code == 200
    updated_client_data = response.json.get('data')
    assert updated_client_data['loyality_balance'] == Decimal('20')