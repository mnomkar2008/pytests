# test-wallet.py
import pytest
from wallet import Wallet

@pytest.mark.parametrize("earned,spent,expected", [
    (120,90,30),
    (200,110,90),
])
def test_wallet_functions(earned,spent,expected):
    wallet = Wallet()
    wallet.deposit(earned)
    wallet.withdraw(spent)
    assert wallet.final_balance() == expected
