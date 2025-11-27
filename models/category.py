"""
Represents a transaction category for income or expense.

"""

class Category:
    # Allowed category names for income
    Income_Categories = ["Salary", "Allowance", "Bonus", "Petty Cash", "Other"]     
    # Allowed category names for expenses
    Expense_Categories = ["transport", "food", "appliances", "health", "beauty", "apparel", "other"]

    # Initialize a new category
    def __init__(self, t_type, c_type):
        # Raise ValueError If the category type is not allowed for the given transaction type.
        if t_type == "expense":
            if c_type not in self.Expense_Categories:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Expense_Categories)}")
            
            self.t_type = t_type    # Transaction type: "income" or "expense"
            self.c_type = c_type    # Category name. Must be in the predefined lists

        elif t_type == "income":
            if c_type not in self.Income_Categories:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Income_Categories)}")
            
            self.t_type = t_type
            self.c_type = c_type

    # Return a readable description of the category type
    def __str__(self):
        return f"{self.t_type} recorded as {self.c_type}"

    # Convert the category object to a dictionary
    def to_dict(self):
        data = {
            "t_type": self.t_type,
            "c_type": self.c_type
        }