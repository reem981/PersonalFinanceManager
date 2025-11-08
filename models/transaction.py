class Transaction:
    def __init__(self, t_type, name, amount, note):
        self.t_type = t_type    #determine if it is #income or #expose transaction
        # self.category = category   #determine the category
        self.name = name
        self.amount = amount
        self.note = note

    def __str__(self):
        print(f"{self.t_type} operation done.\n{self.name} Your Balance Now is: {self.amount} ({self.note})")

    def to_dict(self):
        return {"type": self.t_type, "account name": self.name ,"amount": self.amount, "note": self.note}