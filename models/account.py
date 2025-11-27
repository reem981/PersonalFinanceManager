"""
Represents a personal finance account with a name, password, and balance.
"""
#-----------------------------------------------------------------------------------------
# Account CLASS DEFINITION
#-----------------------------------------------------------------------------------------
class Account:
    # Initialize a new account.
    def __init__(self,name, password, balance = 0):
        if balance < 0:     # check if balance negative
            raise ValueError("Balance Can't Be Negative..\n")
        self._name = name   #  Account owner's name
        self._password =password    # Account password (plain text in this project).
        self._balance = balance     # Initial account balance. Must not be negative.

    @property  # name getter
    def name(self):
        return self._name   # Return the account owner's name

    @property  # balance getter
    def balance(self):
        return self._balance    # Return the current account balance
       

    def add_balance(self, amount):      # Increase the account balance by a positive amount
        if amount <= 0:
            # Raise ValueError # If the amount is zero or negative.
            raise ValueError("The amount must be positive to add.")
        
        self._balance += amount


    def reduce_balance(self, amount):   # Decrease the account balance by a positive amount
        if amount <= 0:     # Amount to be withdrawn. Must be greater than zero and not exceed the current balance
            raise ValueError("The amount must be positive to withdraw.")
        if amount > self._balance:
            raise ValueError("No sufficient balance in your account.")
        self._balance -= amount


    def __str__(self):      # Return a readable string representation of the account.
        return f"Name: {self.name}, Your Account: {self.balance:.2f}"
        
    def to_dict(self):      # Convert the account object to a dictionary
        data= {
            "name": self._name,
            "password": self._password,
            "balance": self._balance
        }
        return data