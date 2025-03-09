from people.person import Person

class Employee(Person):
    def __init__(self, firstname, lastname, payrollno):
        super().__init__(self, firstname, lastname, payrollno)
        self.__payrollno = payrollno

    def get_payrollno(self):
        return self.__payrollno

