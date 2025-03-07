# Employee is a derived class from base class(Person)
from person_details.person import Person

class Employee(Person):
    """ Represents an Employee, inheriting from the Person class.
      This class adds employee-specific attributes like employee ID and position,
      with validation for employee ID."""

    def __init__(self, firstname, lastname, age, employee_id, position):
        """ Initializes an Instance object.
        :param firstname: str - First name of the employee.
        :param lastname: str - Last name of the employee.
        :param age: int - Age of the employee.
        :param employee_id: str - Unique identifier for the employee (must start with a letter).
        :param position: str - Job position of the employee."""
        super().__init__(firstname, lastname, age) # called the super class or base class of employee class,Initialize from Person class
        self._employee_id = employee_id  # Direct assignment no validation
        #self.set_employee_id(employee_id)      # Using setter for validation
        self._position = position

    # getters for emp id and position
    def get_employee_id(self):
        """ Gets the employee's ID.
        :return: str - Employee ID."""
        return self._employee_id

    def get_position(self):
        """ Gets the employee's job position.
        :return: str - Job position."""
        return self._position

   # setters for emp_id and position
    def set_employee_id(self, employee_id):
        """ Sets and validates the employee's ID.
        :param employee_id: str - Must start with an alphabet.
        :raises ValueError: If employee_id does not start with a letter."""
        if employee_id and employee_id[0].isalpha():   # if employee_id checks that is not empty string and Ensure the ID starts with an alphabet
            self._employee_id = employee_id
        else:
            raise ValueError("Employee Id must start with an alphabet")

    def set_position(self, position):
        """Sets the employee's job position.
        :param position: str - Job position."""
        self._position = position

    def __str__(self):
        """Returns a formatted string representation of the Employee object.

        - Calls the `__str__` method of the parent class (`super().__str__()`)
          to include details from the `Person` class (e.g., firstname,lastname, age).
        - Appends Employee-specific details: Employee ID and Position.
        :return: str - Employee details including firstname,lastname, age, ID, and position."""
        return f"{super().__str__()}\nEmployee Id : {self._employee_id}\nPosition : {self._position}"

