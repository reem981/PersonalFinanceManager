class Category:
    Income_Categories = ["Salary", "Allowance", "Bonus", "Petty Cash", "Other"]
    Expense_Categories = ["transport", "food", "appliances", "health", "beauty", "apparel", "other"]
    def __init__(self, t_type, c_type):
        if t_type == "expense":
            if c_type not in self.Category_names:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Expense_Categories)}")
            
            self.name = t_type
            self.c_type = c_type

        elif t_type == "income":
            if c_type not in self.Income_Categories:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Income_Categories)}")
            
            self.name = t_type
            self.c_type = c_type

    def __str__(self):
        return f"{self.t_type} recorded as {self.c_type}"

    def to_dict(self):
        data = {
            "t_type": self.t_type,
            "c_type": self.c_type
        }