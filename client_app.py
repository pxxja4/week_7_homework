from person_details.person import Person
from person_details.employee import Employee
from person_details.customer import Customer

try:
    # Creating a Person object or Instantiation
    person1 = Person('Chaitra', 'Boregowda', 31)
    print(person1)
    print(person1.get_age())
    #print(person1.set_lastname('Tom Jerry'))
    print("~" * 50)
    # Creating an Employee object
    employee1 = Employee('Lisa', 'Simon',35, 'E123', 'Software Engineer')
    print(employee1)
    print("~" * 50)
    #print(employee1.set_employee_id('123'))

    print("~" * 50)
    # Creating a Customer object
    customer1 = Customer('Issa','Bela',40,12)
    print(customer1)
    print("~" * 50)
    print(customer1.set_customer_id(-45))  # prints error message
    # customer2 = Customer('Tom','Jerry',50, 'C123')
    # print(customer2)

except ValueError as er:
    print(er)

except Exception as ex:
    # log the exception to a log file
    print("An Unexpected error has occurred. Please contact tech support")
    print(ex)

finally:
    print("The Finally block always run")