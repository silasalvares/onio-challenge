import pytest
from bson import ObjectId
from decimal import Decimal
from mongoengine import connect, get_connection, disconnect
from mongoengine.errors import DoesNotExist

from app.utils.exeptions import InsuficientBalance
from app.modules.loyality.loyality_models import User
from app.modules.loyality import loyality_service

@pytest.fixture(scope="function")
def connection():
    return connect('mongoenginetest', host='mongomock://localhost')

def test_when_new_user__balance_is_zero(connection):
    new_user = loyality_service.register_user('00000000191')
    assert type(new_user.balance) == Decimal
    assert new_user.balance == Decimal('0')

def test_when_score_requested__user_data_is_returned():
    user_data = loyality_service.get_score('00000000191')
    assert user_data.balance == Decimal('0')

def test_when_user_credited__balance_increase():
    entry_data = loyality_service.credit({'cpf': '00000000191', 'value': 10.0})
    assert entry_data.user.balance == Decimal('10.0')

def test_when_user_debited__balance_is_decreased():
    entry_data = loyality_service.debt({'cpf': '00000000191', 'value': 5.0})
    assert entry_data.user.balance == Decimal('5.0')

def test_when_try_to_update_unregistered_user__it_is_created():
    entry_data = loyality_service.credit({'cpf': '01483535509', 'value': 5.0})
    assert entry_data.user.cpf == '01483535509'
    assert entry_data.user.balance == Decimal('5')

def test_when_insuficient_balance__excpetion_is_thrown():
    with pytest.raises(InsuficientBalance):
        entry_data = loyality_service.debt({'cpf': '00000000191', 'value': 50.0})
