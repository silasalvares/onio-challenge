import pytest
from decimal import Decimal
from mongoengine import connect, disconnect
from app import app


@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture(scope="module")
def connection():
    conn = connect('mongoenginetest', host='mongomock://localhost')
    yield conn
    conn.drop_database('mongoenginetest')


def test_when_credit__data_are_returned(client, connection):
    response = client.post('/', json={
        'cpf': '00000000191',
        'value': 10
    })

    assert response.status_code == 200
    entry_data = response.json.get('data')
    print(entry_data)
    assert entry_data['user']['cpf'] == '00000000191'
    assert entry_data['value'] == Decimal('10')