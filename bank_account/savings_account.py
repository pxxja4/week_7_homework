from bank_account.account import Account

class SavingsAccount(Account):
    """Represents a savings account with interest."""

    def __init__(self,initial_amount, account_number, firstname,lastname, interest_rate=2):
        super().__init__(initial_amount, account_number, firstname, lastname)
        self.interest_rate = interest_rate  # Public attribute

    # Apply interest to the balance
    def apply_interest(self):
        if self.interest_rate > 0:
            interest = self.get_balance() * (self.interest_rate / 100)  # Using get_balance() because the _balance is private cannot be accessed directly
            self.deposit(interest)   # Add interest to balance
            print(f"Interest applied: ${interest:.2f}. New balance: ${self.get_balance():.2f}")  # Formats the output to 2 decimal places
        else:
            raise ValueError("Interest rate must be positive.")

    def __str__(self):
        # Display interest rate
        return f"{super().__str__()}\nInterest Rate: {self.interest_rate:.1f} %"
