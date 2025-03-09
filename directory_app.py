from people.customer import Customer
from people.employee import Employee

try:
    bill_customer = Customer('bill', 'smith', 222333)
    print(bill_customer)

    print(bill_customer.get_customerreferenceno())


    erica_employee = Employee('erica', 'jones', 343535)
    print(erica_employee)
    print(erica_employee.get_payrollno())

finally:
    print('Thank you for accessing the directory')