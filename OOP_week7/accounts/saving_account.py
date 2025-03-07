# explicit inheritance
from account import Account

class SavingsAccount(Account):
    def __init__(self, initial_amount, firstname, lastname, interest_rate, permitted_withdrawals):
        super().__init__(initial_amount, firstname, lastname)
        self.__balance = initial_amount
        self.__firstname = firstname
        self.__lastname = lastname
        self.__interest_rate = interest_rate
        self.__permitted_withdrawals = permitted_withdrawals

    def get_attributes(self):
        attributes = super().get_attributes()
        attributes["Interest rate (annual)"] = self.__interest_rate
        attributes["Permitted withdrawals per annum:"] = self.__permitted_withdrawals

    def __str__(self):
            #         method was inherited from objected and i am overriding it
            return f"bank account holder: {self.firstname} {self._lastname}\nHas balance: ${self.get_balance()}.The annual interest rate for this account is {self.__interest_rate}% and you can withdraw {self.__permitted_withdrawals} times every year."