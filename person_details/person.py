# a class is a template / blueprint
# we create objects of the class type -> instantiation
# 2 things : DATA and BEHAVIOUR,
# A constructor (__init__ method) is used to initialize an object's attributes when an instance of a class is created.
# Setters are special methods used to control how attributes are modified after an object is created.
# For validation or encapsulation(data protection)

class Person:
    # Initialize a Person object with first name, last name, and age
    def __init__(self, firstname, lastname, age, gender, contact_number=None):
        self._firstname = firstname  # _firstname is a protected attribute.Can access within this class and by subclasses but not directly from outside.
        self._lastname = lastname   # they should not be accessed directly from outside the class,but they are still accessible.
        self._age = age
        self.__gender = gender    # __gender is private 
        self.set_contact_number(contact_number) # Contact number is set as a setter method,which allows validation .
        #self._contact_number = contact_number

    # property - Getters for firstname, lastname and age
    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_age(self):
        return self._age

    # Getter for gender (no setter, so it can't be changed,private variable)
    def get_gender(self):
        return self.__gender

    def get_contact_number(self):
        return self._contact_number

   # setter for the firstname
    def set_firstname(self, first_name):
        if str(first_name).isalpha():
            self._firstname = first_name
            return self._firstname
        else:
            # instantiating a ValueError object and throwing it
            raise ValueError("Lastname must be alphabetic")

    # Setter for the last name (only alphabetic last names are allowed,no special character,spaces)
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
            return self._lastname
        else:
            # instantiating a ValueError object and throwing it
            raise ValueError("Lastname must be alphabetic")

    # setter for age
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
            return self._age
        else:
            raise ValueError("Age must be positive integer")

    def set_contact_number(self, contact_number):
        if isinstance(contact_number, str) and contact_number.isdigit() and len(contact_number) == 10:
            self._contact_number = contact_number
        else:
            raise ValueError("Contact number should be a string of digits with 10-digit number.")


    # print the string representation of the person-shows name and age.
    def __str__(self):
        return f"Name : {self._firstname} {self._lastname}\nAge : {self._age}\nGender: {self.__gender}\nContact Number : {self._contact_number}"


