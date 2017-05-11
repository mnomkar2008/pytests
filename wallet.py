
class NotEnoughMoney(Exception):
    pass

class Wallet(object):

    def __init__(self, amount=0):
        self.balance = amount

    def final_balance(self):
        return self.balance

    def deposit(self, amount=0):
        self.balance += amount
        return self.balance

    def withdraw(self, amount=0):
        if self.balance < amount:
            raise NotEnoughMoney("Less balance than amount to spend, cannot withdraw..")

        self.balance -= amount
        return self.balance


def main():
    print "in main : "
    moneyObj = Wallet(1200)
    print "Balance in my account :", moneyObj.final_balance()

    # Making deposit to the account
    moneyObj.deposit(2800)
    print "After deposit, balance in my account :", moneyObj.final_balance()
    moneyObj.withdraw(5000); print "After deposit, balance in my account :", moneyObj.final_balance()
    # Withdrawing deposit from the account
    #moneyObj.withdraw(3000)
    #print "After deposit, balance in my account :", moneyObj.final_balance()

if __name__ == '__main__':
  main()
