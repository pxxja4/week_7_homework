from person_details.person import Person
from person_details.employee import Employee
from person_details.customer import Customer

try:
    # Creating a Person object or Instantiation
    person1 = Person('Andy', 'Williams', 31, 'Male','9456789890')
    print(person1)
    print("~" * 50)

    print(person1.get_age())
    print(person1.get_contact_number())
    print(person1.set_age(25))
    #print(person1.set_lastname('Tom Jerry'))
    print("~" * 50)

    # Creating an Employee object
    employee1 = Employee('Lisa', 'Simon', 35, 'Female','9456789120','E12DEV05', 'Software Engineer')  # this will raise an error
    print(employee1)
    print("~" * 50)
    # employee2 = Employee('Lisa', 'Simon',35,'Female','9456789120', 123, 'Software Engineer')  # this will raise an error
    # print(employee2)
    print("~" * 50)
    print(employee1.get_employee_id())
    print("~" * 50)
    # trying to modify the employee_id (raise an error)
    # employee1.set_employee_id('b345')
    # print(employee1)

    employee1.set_position('Senior Engineer')
    print(employee1)

    print("~" * 50)
    # Creating a Customer object
    customer1 = Customer('Issa','Bela',40,'Female','9456789120',12)
    print(customer1)
    print("~" * 50)
    customer1.set_lastname('khan')
    print(customer1)

    #print(customer1.set_customer_id(-45))  # raise error message
    # customer2 = Customer('Tom','Jerry',50, 'C123')
    # print(customer2)  # raise error

except ValueError as er:
    print(f"Error: {er}")

except Exception as ex:
    # log the exception to a log file
    print("An Unexpected error has occurred. Please contact tech support")
    print(f"Error: {ex}")

finally:
    # This block will always run, whether an exception occurred or not.
    print("~" * 50)
    print("The Finally block always run")