import pytest
from wallet import Wallet, NotEnoughMoney

# Fixtures are used to remove boilerplate code
@pytest.fixture
def empty_wallet():
    """
    Returns a wallet instance with empty balance.
    """
    return Wallet()

@pytest.fixture
def set_wallet():
    """
    Returns a wallet instance with a initial balance of 30.
    """
    return Wallet(30)

def test_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_set_amount(set_wallet):
    assert set_wallet.balance == 30

def test_deposit_amount(empty_wallet):
    empty_wallet.deposit(120)
    assert empty_wallet.balance == 120

def test_withdraw_amount(set_wallet):
    set_wallet.withdraw(10)
    assert set_wallet.balance == 20

def test_exception_error(set_wallet):
    with pytest.raises(NotEnoughMoney):
        set_wallet.withdraw(10000)
