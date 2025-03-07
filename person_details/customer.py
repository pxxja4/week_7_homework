# Customer is a derived class from Person base class
from person_details.person import Person

class Customer(Person):
      def __init__(self, firstname, lastname, age, customer_id):
          super().__init__(firstname, lastname, age)
          #self.set_customer_id(customer_id)
          self._customer_id = customer_id

      # getters
      def get_customer_id(self):
          return self._customer_id

      # setters
      def set_customer_id(self, customer_id):
          if not isinstance(customer_id, int) or customer_id < 0:
              raise ValueError("Customer ID must be a positive integer.")
          else:
              self._customer_id = customer_id


      def __str__(self):
          return f"{super().__str__()}\nCustomer_Id : {self._customer_id}"