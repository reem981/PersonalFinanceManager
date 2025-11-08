class account:
    name = ""
    balance = 0
    # cash_wallet = 0
    # credit_card = 0
    # savings_account = 0

    def __init__(self,name, balance):
        self.name = name
        self.balance =balance
        # self.cash_wallet = cash_wallet
        # self.credit_card = credit_card
        # self.savings_account = savings_account

    def add_balance(self, amount):
        self.balance += amount
    
    # def add_cash_balance(self, amount):
    #     self.cash_wallet += amount

    # def add_credit_balance(self, amount):
    #     self.credit_card += amount

    # def add_saving_balance(self, amount):
    #     self.savings_account += amount

    def reduce_balance(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("No Such Balance in Your Account. ❌")
    
    # def reduce_cash_balance(self, amount):
    #     if amount < self.Bank_account:
    #         self.cash_wallet -= amount
    #     else:
    #         print("This Amount Does Not Exists In Your Account..")

    # def reduce_credit_balance(self, amount):
    #     if amount < self.Bank_account:
    #       self.credit_card -= amount

    # def reduce_saving_balance(self, amount):
    #     if amount < self.Bank_account:
    #         self.savings_account -= amount

    def __str__(self):
        print(f"Name: {self.name}, Your Account: {self.balance}")
        
    def to_dict(self):
        data= {
            "name": self.name,
            "balance": self.balance
        }
        return data