from ex_16_OOP import person_class
from week_7_homework.ex_16_OOP.person_class import Person
from week_7_homework.ex_16_OOP.employee_class import Employee
from week_7_homework.ex_16_OOP.customer_class import Customer
from accounts.account import Account

person_1 = Person('Francesca', 'Puccini', 30, 'F', "italian")

print(person_1.get_personal_details())
print(person_1.get_person_passport_details())
person_2 =  Person("Jason", "Smith", 40, 'M', "British")
print(person_2)

print("#" * 100 )
employee_1 = Employee("Serena", 'Gallinotti', "project manager", 'sgt19076', 2000)
print(employee_1)
print(employee_1.set_employee_signature())

# try:
#     print("#" *100)
#     customer_1 = Customer('John', 'Danks', 'john.danks@gmail.com', 1000, 8989899)
#     print(customer_1.get_customer_details())
#
