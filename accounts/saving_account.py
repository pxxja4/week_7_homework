# explicit inheritance - inherit features from bank account
from accounts.account import Account
# looks like passing Account class as parameter
# a saving account is a 'kind of' account

# account class is a base/super class/ parent class
# saving account class is a derived class / subclass or child class

# for savings account object to exist

class SavingAccount(Account):
    def __init__(self, super, initial_amount, firstname, lastname, interest_rate):
        super.__init__(self, initial_amount, firstname, lastname, interest_rate )
        self.interest_rate = interest_rate
 # add interest rates/ methods etc

    def add_interest(self):
        return int(self.interest_rate) * super(self.initial_amount)
        print (f'Your new balance is {self.getbalance()}')

    def withdraw(self, amount):
        new_balance = self.__balance
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        else:
            self.__balance = self.__balance - amount
            print(f'Your new balance is {self.__balance}')
