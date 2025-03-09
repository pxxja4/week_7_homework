class Employee:
    # we instantiate a class by using the constructor __init__
    #  we define some attribute to the class as parameters
    def __init__(self, firstname, lastname, jobrole, employeeid, salary):
        self.firstname = firstname
        self._lastname = lastname
        self.jobrole = jobrole
        self.__employeeID = employeeid
        self.__salary = salary


    # we use getter and setter to encapsulate the attributes of the class
    def get_employee_details(self):
        return self.firstname.upper, self._lastname, self.jobrole, self.__employeeID

    def get_employee_salary(self):
        return self.__salary

    # for sensitive information that we don't be modified then we only use getter which provides read only access to the attributes of the class
    def get_employeeid(self):
        return self.__employeeID


    def set_employee_signature(self):
        return(f'Kind regards,\n {self.firstname} {self._lastname}, {self.jobrole.upper()}')

    def __str__(self):
        # overrides an inherited method
        return f" Here is the employee details: {self.firstname.upper()},{self._lastname.upper()}  {self.jobrole}"
