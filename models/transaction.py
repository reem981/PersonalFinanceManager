"""
Represents a single financial transaction
"""

from datetime import datetime
class Transaction:
    # Initialize a new transaction
    def __init__(self, t_type, category, owner, amount, note):
        self.t_type = t_type    #determine if it is #income or #expose transaction
        self.category = category   #determine the category name
        self.owner = owner            #determin the owner of the account
        self.amount = amount    # Transaction amount
        self.note = note    # Optional note or description
        self.date = datetime.now().strftime("%Y-%m-%d")     # Transaction date in 'YYYY-MM-DD' format

    # Return a readable summary of the transaction
    def __str__(self):
        return f"{self.t_type} operation done.\n{self.owner} Your Amount: {self.amount} ({self.note})"

    # Convert the transaction object to a dictionary
    def to_dict(self):
        return {
            "type": self.t_type,  
            "category": self.category ,
            "account owner": self.owner ,
            "amount": self.amount, 
            "note": self.note, 
            "date": self.date
                }