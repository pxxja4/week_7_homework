from OOP_week7.accounts import saving_account
from account import Account
from saving_account import SavingsAccount

# instantiate an object through indirectly calling a method
# a special method called __init__ gets called - a CONSTRUCTOR
try:
    # try block = everything I want my programme to do/try first
    # lisa_account = Account(500, "Lisa", "Simpson")
    # print(lisa_account)
    # print(type(lisa_account))

    # 1. create class
    # 2. instantiate
    # 3. dot notation
    #
    # # if i do not say what kind of class i am creating, it inherits from object (which is a class in Python)
    # bart_account = Account(100, "Bart", "Simpson")
    # print(bart_account)

    # here is where i cosntructed a amggie_savings objects which is a sub class of Account. It has two additional attributes.
    print("********************************")
    maggie_savings = SavingsAccount(100, "Maggie", "Simpson", 3.35, 2)
    print(maggie_savings)
    print("********************************")

    maggie_savings.withdraw_savings(200)
#     here i am using a method to withdraw more than maggie ahs from her account

# except Exception as ex:
#     # log the exception to a log file
#     print ("Please contact tech support")
#     print(ex)

except ValueError as ex:
    print(ex)
#     value error to be returned if Maggie wants to withdraw more than she has in her bank account

finally:
    print("Thank you for banking with us today.")
