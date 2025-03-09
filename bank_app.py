from traceback import print_tb

from accounts.account import Account
from accounts.saving_account import SavingAccount

# instantiate an object
# indirectly calling a method. Special method called __init__ gets called
# it is a constructor
try:
    lisa_account = Account(500, 'Lisa', "simpson")
    print(lisa_account)
    print(type(lisa_account))

    bart_account = Account(25, 'Bart', 'Simpson')
    print(bart_account)
    print(type(bart_account))

    # lisa_account.

    print(lisa_account.get_balance())

    print(lisa_account.get_lastname())

    print(lisa_account.firstname)
    lisa_account.firstname = 241432434

    print(lisa_account.firstname)
    print(lisa_account.get_lastname())
    lisa_account.set_lastname('VanOuten')
    print(lisa_account.get_lastname())

    bart_account.set_lastname('Flanders')

    print(lisa_account)
    print(bart_account)

    bart_account.deposit(100)
    print("#" * 30)
    print(bart_account)

    print('*****************')

    maggie_account = Account(80, 'Maggie', 'Simpson')
    print(maggie_account)

    maggie_account.withdraw(5)
    print(maggie_account)

    lisa_saving = SavingAccount()
    print(lisa_saving)
    print(type(lisa_saving))
    lisa_saving.deposit(50)

except ValueError as ex:
    # log exception to a log file. Open function, appending, record error
    print("An error has occurred")
    print(ex)
except Exception as ex:
    # generic
    print("An unexpected error has occurred. Please contact tech support")
    print(ex)
finally:
    print('The FINALLY BLOCK ALWAYS RUNS')

