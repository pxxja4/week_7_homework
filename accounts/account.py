# create class. A class is a blueprint/ template
# create objects of the class type -> instantiate
# class have 2 things: DATA and BEHAVIOUR
# data aka attributes or properties
# behaviour aka methods
# a method is just a function that belongs to a class
# example: student class
# data: firstname, lastname, email, cohort_number NOUNS
# behaviour: attend_learning_session, book_timeslot VERB

# if we do not say what 'kind of' class our class is
# it implicitly inherits from 'object'. There is a class in python called object

# f for field - piece of data/ coloumn

# self is implicitly passed in
# takes 3 arguments and then assigns them to a field in box of memory
# underscores have significance to python - visibility outside of the class
# class is capsule. Do we need to be inside capsule to see the stuff or can we be outside and still see it
# hiding things - which is good. Making things less complex. From design perspective, less outside world sees and depends on it
# don't want outside world to poke/ prod at code. can't refactor stuff if they are using it
# encaspulate: no underscore, 1 or 2
# no underscore  - public - can be changed by outside world
# single underscore: semi private (protected)
# double underscore: private


class Account:

    def __init__(self, initial_amount, firstname, lastname):
        self.__balance = initial_amount
        self.firstname = firstname
        self._lastname = lastname

# getters and setters
# getters enable READ access to fields
# setters enable WRITE access to fields
# balance is hidden, we can't let people change their own balances. Users can only read their balance so only make getter
# setter and no getter - eg doing exam, can write and submit but not view answers

    # getters might also contain translation logic
    # eg vehicle - speed mph, but in europe want to see in kph - translate to how its seen by user
    def get_balance(self):
        return self.__balance

    def get_lastname(self):
        return self._lastname.upper()

    # setters often also contain validation logic
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
        else:
            # instantiating a valueerror object and throwing it
            raise ValueError('Lastname must be alphabetic')

        # raise - exception handling. Different classes for errors that can be raised
        # exceptions are usually something exceptional (bad) has happened. Need option to deal with it
        # so they are classes - behaviours, data etc.
        # exception can be thrown and it can be caught - superpower
        # raise throws exception, accept block catches the exception

    #     this is a preset method in the class to make the objject into a string
    # the fancy stuff is saying it's overridin preset stuff
    # overriding an inherited method
    def __str__(self):
        # we are in the capsule atm so we can see the private fields too. Best practice is to use getters because they might have translational element
        return f'Bank Account Holder: {self.firstname} {self._lastname}\nHas balance: £{self.get_balance()}'

# behavioural methods
# deposit
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        new_balance = self.__balance
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        else:
            self.__balance = self.__balance - amount
            print(f'Your new balance is {self.__balance}')