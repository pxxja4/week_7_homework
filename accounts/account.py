class Account:
    # pass- a placeholder to add code later
#
    def __init__(self,  firstname, lastname, initial_amount,):
        self.__balance = initial_amount # private
        self.firstname = firstname   # public
        self._lastname = lastname    # semi-public
# _ prefixed underscore : _ private to class
# encapsulate

    def get_balance(self):
        return self.__balance

    def get_lastname(self):
        return self._lastname.upper()

    # setters often contains validation logic
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
        else:
            # instantiating a ValueError object and throwing
            raise ValueError( 'lastaname must be alphabetic')

#         excpetions: are classes ( they can be catch= exception block and throw= raise)

    def __str__(self):
        # overrides an inherited method
        return f'Bank account holder: {self.firstname} {self._lastname}\n has balance: ${self.get_balance()}'

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

        if amount > self.__balance:
                raise ValueError("Insufficient balance")
        else:
                self.__balance = self.__balance - amount
                print(F'Your balance is: {self.__balance}')
