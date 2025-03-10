from bank_account.custom_exceptions import InsufficientFundsException

class Account:
    # pass   #keyword and placeholder.

    def __init__(self, initial_amount, account_number, firstname, lastname):  # self is a keyword where it is there always (best practice is hide everything)
        if not isinstance(account_number, str) or not account_number[0].isalpha() or not len(account_number)== 10:
            raise ValueError("Account number must be a string starting with an alphabet and 10 characters long.")
        self.__account_number = account_number # private attribute,Cannot be easily accessed or modified from outside the class
        self.__balance = initial_amount  # private
        self.firstname = firstname  # completely visible to the outside world - public
        self._lastname = lastname  # protected,they should not be accessed directly from outside the class,but they are still accessible.

    #   getters and setters
    # getters enable READ access to fields
    # setters enable WRITE access to fields

    # getters might also contain translation logic
    def get_account_number(self):
            return self.__account_number

    def get_balance(self):
        return self.__balance

    #    no setter for balance

    def get_lastname(self):
        return self._lastname.upper()

    # setters often also contain validation logic
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
        else:
            # instantiating a ValueError object and throwing it
            raise ValueError("Lastname must be alphabetic")

    # overriding an inherited method
    def __str__(self):
        return f"Bank Account holder: {self.firstname} {self._lastname}\nAccount Number : {self.__account_number}\nHas balance: ${self.get_balance():.2f}"

    #   behavioural methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            return f"Deposit successful. New balance: ${self.__balance:.2f}"
            #print(f"Deposit successful. New balance: ${self.__balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            #raise InsufficientFundsException()
            raise InsufficientFundsException(f"Cannot withdraw ${amount}. Available balance: ${self.__balance}")
        self.__balance = self.__balance - amount