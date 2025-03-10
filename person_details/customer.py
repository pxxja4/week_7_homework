# Customer is a derived class from Person base class
from person_details.person import Person

class Customer(Person):
      """ Represents a Customer, inheriting from Person class.
            This class adds customer-specific attributes like customer ID and validates the ID."""

      def __init__(self, firstname, lastname, age, gender, contact_number, customer_id):
          super().__init__(firstname, lastname, age, gender, contact_number)
          if not isinstance(customer_id, int) or customer_id < 0:
              raise ValueError("Customer ID must be a positive integer.")
          else:
              self.__customer_id = customer_id  # private variable cannot be modified

      # getters
      def get_customer_id(self):
          return self.__customer_id

      # setters
      def set_customer_id(self, customer_id):
          raise ValueError("Customer ID cannot be modified once set!")

      def __str__(self):
          return f"{super().__str__()}\nCustomer Id : {self.__customer_id}"