from datetime import datetime

# Print a monthly report for a specific user.
# The report shows:
#     - total income
#     - total expenses
#     - net balance (income - expenses)
#     - income grouped by category
#     - expenses grouped by category

def monthly_report(data, month, username):
    transactions = data.get("transactions", [])
    data_of_the_month = [trans for trans in transactions if trans["date"].startswith(month) and trans["account owner"] == username]

    income = sum(trans["amount"] for trans in data_of_the_month if trans["type"] == "income" and trans["account owner"] == username)

    expense = sum(trans["amount"] for trans in data_of_the_month if trans["type"] == "expense" and trans["account owner"] == username)

    print(f"\n The Report for {month} - {username}")
    print(f"Income: {income:.2f}")
    print(f"Expenses: {expense:.2f}")
    print(f"Total Balance: {income - expense:.2f}")

    income_categories = {}
    expenses_categories = {}

    for trans in data_of_the_month:
        if trans["type"] == "expense":
            expenses_categories[trans["category"]] = expenses_categories.get(trans["category"], 0) + trans["amount"]

        elif trans["type"] == "income":
            income_categories[trans["category"]] = income_categories.get(trans["category"], 0) + trans["amount"]

    print("\nExpenses by Category:")
    for cat, total in expenses_categories.items():
        print(f" -{cat}: {total:.2f}")
    
    print("-"*20)

    print("Income by Category:")
    for cat, total in income_categories.items():
        print(f" -{cat}: {total:.2f}")
    print("-"*20)