from datetime import datetime
class Transaction:
    def __init__(self, t_type, category, owner, amount, note):
        self.t_type = t_type    #determine if it is #income or #expose transaction
        self.category = category   #determine the category name
        self.owner = owner            #determin the owner of the account
        self.amount = amount
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.t_type} operation done.\n{self.owner} Your Amount: {self.amount} ({self.note})"

    def to_dict(self):
        return {
            "type": self.t_type,  
            "category": self.category ,
            "account owner": self.owner ,
            "amount": self.amount, 
            "note": self.note, 
            "date": self.date
                }