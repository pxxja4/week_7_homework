# Employee is a derived class from base class(Person)
from person_details.person import Person

class Employee(Person):
    """ Represents an Employee, inheriting from the Person class.
      This class adds employee-specific attributes like employee ID and position,
      with validation for employee ID."""

    def __init__(self, firstname, lastname, age, gender, contact_number, employee_id, position):
        """ Initializes an Instance object.
        :param firstname: str - First name of the employee.
        :param lastname: str - Last name of the employee.
        :param age: int - Age of the employee.
        :param employee_id: str - Unique identifier for the employee (must start with a letter).
        :param position: str - Job position of the employee."""
        super().__init__(firstname, lastname, age, gender, contact_number) # called the super class or base class of employee class,Initialize from Person class

        # The isinstance() function is used to check if an object is an instance of a particular class,here is str
        if not isinstance(employee_id, str):
            raise ValueError("Employee Id must be a string")
        # checks that the employee_id is non-empty and that its first character is an alphabet
        if not employee_id or not employee_id[0].isalpha():
            raise ValueError("Employee Id must start with an alphabet")
        self.__employee_id = employee_id  # set only once no setter for employee id ,private attribute
        self._position = position

    # getters for emp id and position
    def get_employee_id(self):
        """ Gets the employee's ID.
        :return: str - Employee ID."""
        return self.__employee_id

    def get_position(self):
        """ Gets the employee's job position.
        :return: str - Job position."""
        return self._position

    def set_employee_id(self, employee_id):
        """ Raise an error if trying to modify the employee ID."""
        raise ValueError("Employee ID cannot be modified once set!")

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
        return f"{super().__str__()}\nEmployee Id : {self.__employee_id}\nPosition : {self._position}"

