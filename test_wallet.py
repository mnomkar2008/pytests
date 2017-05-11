import pytest
from wallet import Wallet, NotEnoughMoney


def test_default_initial_amount():
    #import pdb; pdb.set_trace()
    walletObj = Wallet()
    assert walletObj.balance == 0

def test_deposit_amount():
    # import pdb; pdb.set_trace()
    walletObj = Wallet(90)
    walletObj.deposit(120)
    assert walletObj.balance == 210

def test_withdraw_amount():
    # import pdb; pdb.set_trace()
    walletObj = Wallet(100)
    walletObj.withdraw(10)
    assert walletObj.balance == 90

def test_exception_error():
    walletObj = Wallet(100)
    with pytest.raises(NotEnoughMoney):
        walletObj.withdraw(10000)