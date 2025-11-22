class Account:

    def __init__(self,name, password, balance = 0):
        if balance < 0:     # check if balance negative
            raise ValueError("Balance Can't Be Negative..\n")
        self._name = name
        self._password =password
        self._balance = balance

    @property  # name getter
    def name(self):
        return self._name

    @property  # balance getter
    def balance(self):
        return self._balance
       

    def add_balance(self, amount):      # check if the amount is positive before adding
        if amount <= 0:
            raise ValueError("The amount must be positive to add.")
        
        self._balance += amount


    def reduce_balance(self, amount):
        if amount <= 0:
            raise ValueError("The amount must be positive to withdraw.")
        if amount > self._balance:
            raise ValueError("No sufficient balance in your account.")
        self._balance -= amount


    def __str__(self):
        return f"Name: {self.name}, Your Account: {self.balance:.2f}"
        
    def to_dict(self):
        data= {
            "name": self._name,
            "password": self._password,
            "balance": self._balance
        }
        return data