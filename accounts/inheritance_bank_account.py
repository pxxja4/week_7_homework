from account import Account

class Inheritance_Account(Account):
        def __init__(self, balance, firstname, lastname, bonus=0):
            super().__init__(balance, firstname, lastname)  # Call parent constructor
            self.bonus = bonus  # New attribute

        def apply_bonus(self):
            """Adds the bonus to the account balance."""
            self.deposit(self.bonus)
            self.bonus = 0  # Reset bonus after applying

        def __str__(self):
            return f"{super().__str__()}, Bonus: {self.bonus}"




