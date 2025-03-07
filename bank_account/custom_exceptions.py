# Custom Exception- created our own exception and it is a derived class from Exception parent class

class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds in the account."""
    def __init__(self, message="Insufficient funds in the account"):
        super().__init__(message)