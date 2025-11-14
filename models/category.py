class Category:
    Income_Categories = ["Salary", "Allowance", "Bonus", "Petty Cash", "Other"]
    Category_names = ["transport", "food", "appliances", "health", "beauty", "apparel", "other"]
    def __init__(self, name, c_type):
        if name == "expense":
            if c_type not in self.Category_names:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Category_names)}")
            
            self.name = name
            self.c_type = c_type

        elif name == "income":
            if c_type not in self.Income_Categories:
                raise ValueError(f"Category Type Should Be One Of These Types: {','.join(self.Income_Categories)}")
            
            self.name = name
            self.c_type = c_type

    def __str__(self):
        print(f"{self.name} recorded as {self.c_type}")

    def to_dict(self):
        data = {
            "name": self.name,
            "c_type": self.c_type
        }