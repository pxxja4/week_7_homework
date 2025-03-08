# explicit inheritance
from account import Account

class SavingsAccount(Account):
    # defning a new sub class, all of its attributes
    def __init__(self, initial_amount, firstname, lastname, interest_rate, permitted_withdrawals):
        super().__init__(initial_amount, firstname, lastname)
        self.__balance = initial_amount
        self.__firstname = firstname
        self.__lastname = lastname
        self.__interest_rate = interest_rate
        self.__permitted_withdrawals = permitted_withdrawals
    # fetching the super attributes and adding to them the two additional ones which my savingsaccount class has
    def get_attributes(self):
        attributes = super().get_attributes()
        attributes["Interest rate (annual)"] = self.__interest_rate
        attributes["Permitted withdrawals per annum:"] = self.__permitted_withdrawals

    def __str__(self):
            # ensuring strings are returned to the user to display the message
            return f"bank account holder: {self.firstname} {self._lastname}\nHas balance: ${self.get_balance()}.The annual interest rate for this account is {self.__interest_rate}% and you can withdraw {self.__permitted_withdrawals} times every year."

    # definitn a method to withdraw from the account
    def withdraw_savings(self, amount):
            if amount > self.__balance:
                raise ValueError("You can't withdraw more than you have in the account. Please try another amount.")
            # this is where i define my value error
            else:
                self.__balance -= amount
                print(f"Your new balance is: {self.__balance}")



