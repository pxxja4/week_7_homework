from account import Account
from saving_account import SavingsAccount

# instantiate an object through indirectly calling a method
# a special method called __init__ gets called - a CONSTRUCTOR
try:
    # try block = everything I want my programme to do/try first
    lisa_account = Account(500, "Lisa", "Simpson")
    print(lisa_account)
    print(type(lisa_account))

    # 1. create class
    # 2. instantiate
    # 3. dot notation
    #
    # # if i do not say what kind of class i am creating, it inherits from object (which is a class in Python)
    # bart_account = Account(100, "Bart", "Simpson")
    # print(bart_account)
    #
    # maggie_account = Account(80, "Maggie", "Simpson")
    # print(maggie_account)
    #
    #


    print("********************************")
    maggie_savings = SavingsAccount(100, "Maggie", "Simpson", 3.35, 2)
    print(maggie_savings)
    print("********************************")

except ValueError as ex:
    # log the exception to a log file
    print("An error has occurred")
    print(ex)

except Exception as ex:
    # log the exception to a log file
    print ("Please contact tech support")
    print(ex)

finally:
    print("The finally block always runs")
