# a template/blueprint for a objects which will be later created based on it (of the class type)
# creating an object based on a class = instantiating
# classes have: data & behaviour
# data = attributes / properties
# behaviour = methods
# a method is just a function that belongs to a class

# python keyword to act as placeholder, putting it on hold just now
# data: name, cohort, email
# behaviour: attended_session, booked_slot

class Account:
    def __init__(self, initial_amount, firstname, lastname):
        #         self is a python key word for all objects/methods
        # passed implicitely when a class method is called, shared by all objects of this class
        self.__balance = initial_amount
        self.firstname = firstname
        self._lastname = lastname
# here, all of the variables are assigned a place in the class i.e (firstname gets a self.firstname place)
# no underscore = public/visible to outside world
# 1 under = semi-private
# __ at the start  = private
# underscores signify visibility outside of the encapsulation

# getters and setters
# getters = read access to fields
# setters = enable writing access to fields

    def get_balance(self):
        return self.__balance
#     getters might also contain translation logic

    def get_lastname(self):
        return self._lastname.upper()

    # setters often contain validation logic
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
        else:
            # instantiating a valueError object and throwing it
            raise ValueError("Lastname must be alphabetic")

    def __str__(self):
#         method was inherited from objected and i am overriding it
        return f"bank account holder: {self.firstname} {self._lastname}\nHas balance: ${self.get_balance()}"


    # behavioral methods
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
            if amount > self.__balance:
                raise ValueError("Insufficient funds on the account.")
            else:
                self.__balance = self.__balance - amount
                print(f"Your new balance is: {self.__balance}")


