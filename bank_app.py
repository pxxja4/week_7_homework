from bank_account.account import Account
from bank_account.custom_exceptions import InsufficientFundsException
from bank_account.savings_account import SavingsAccount

try:
    account1 = Account(500, 'A123456789', 'Trina', 'Thomas')
    print(account1)
    print("~" * 50)
    #print(account1.get_account_number())
    #print(account1.get_balance())
    account1.deposit(500)
    print(account1)
    print("~" * 50)
    #account1.withdraw(1500)  # Withdraw amount larger than balance, raise InsufficientFundsException
    #print(account1)
    print("~" * 50)
    # Creating a savings account
    savings_acc = SavingsAccount(2000,'A123456789','Lisa','Tom')
    savings_acc.apply_interest()
    print(savings_acc)

except ValueError as er:
    # log the exception to a log file,If a ValueError occurs, this block will handle it
    print("An error has occurred")
    print(er)

except InsufficientFundsException as er:
    # If InsufficientFundsException occurs, this block will handle it.
    print(f"Insufficient fund in the account,{er}")

except Exception as ex:
    # Any other unexpected exceptions will be caught here.
    print("An Unexpected error has occurred. Please contact tech support")
    print(ex)

finally:
    # This block will always run, whether an exception occurred or not.
    print("~" * 50)
    print("The Finally block always run")
