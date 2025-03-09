class Customer:

    def __init__(self, firstname, lastname,email, initial_amount, account_number):
        self.firstname = firstname
        self._lastname = lastname
        self.__email = email
        self.__initial_amount = initial_amount
        self.__account_number = account_number

    def get_customer_details(self):
        return self.firstname, self._lastname,self.__email,

    def get_account_details(self):
        return f"The account details are : £{self.__initial_amount} for the account :{self.__account_number}"


