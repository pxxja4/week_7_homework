# a class is a template / blueprint
# we create objects of the class type -> instantiation
# 2 things : DATA and BEHAVIOUR,
# A constructor (__init__ method) is used to initialize an object's attributes when an instance of a class is created.
# Setters are special methods used to control how attributes are modified after an object is created.
# For validation or encapsulation(data protection)

class Person:
    # Initialize a Person object with first name, last name, and age
    def __init__(self, firstname, lastname, age):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age

    # property - Getters for firstname, lastname and age
    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_age(self):
        return self._age

   # setter for the firstname
    def set_firstname(self, first_name):
        self._firstname = first_name

    # Setter for the last name (only alphabetic last names are allowed,no special character,spaces)
    def set_lastname(self, last_name):
        if str(last_name).isalpha():
            self._lastname = last_name
        else:
            # instantiating a ValueError object and throwing it
            raise ValueError("Lastname must be alphabetic")
    # setter for age
    def set_age(self, age):
        self._age = age

    # print the string representation of the person-shows name and age.
    def __str__(self):
        return f"Name : {self._firstname} {self._lastname}\nAge : {self._age}"


