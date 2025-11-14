class account:
    name = ""
    balance = 0

    def __init__(self,name, balance):
        if balance < 0:
            raise ValueError("Balance Can't Be Negative..\n")
        self.name = name
        self.balance =balance

    def add_balance(self, amount):
        if amount < 0:
            print("The Amount Can't Be Negative..")
        else:
            self.balance += amount
    

    def reduce_balance(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("No Such Balance in Your Account. ❌")
 

    def __str__(self):
        print(f"Name: {self.name}, Your Account: {self.balance:.2f}")
        
    def to_dict(self):
        data= {
            "name": self.name,
            "balance": self.balance
        }
        return data