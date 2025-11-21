from datetime import datetime

def monthly_report(data, month, username):
    transactions = data.get("transactions", [])
    data_of_the_month = [trans for trans in transactions if trans["date"].startswith(month) and trans["account name"] == username]

    income = sum(trans["amount"] for trans in data_of_the_month if trans["type"] == "income" and trans["account name"] == username)

    expense = sum(trans["amount"] for trans in data_of_the_month if trans["type"] == "expense" and trans["account name"] == username)

    print(f"\n The Report Of {month} for {username}")
    print(f"Income: {income:.2f}")
    print(f"Expenses: {expense:.2f}")
    print(f"Total: {income - expense:.2f}")

    print("\nCategories Of The Expenses: ")
    income_categories = {}
    expenses_categories = {}

    for trans in data_of_the_month:
        if trans["type"] == "expense":
            expenses_categories[trans["category"]] = expenses_categories.get(trans["category"], 0) + trans["amount"]

        elif trans["type"] == "income":
            income_categories[trans["category"]] = income_categories.get(trans["category"], 0) + trans["amount"]

    for cat, total in expenses_categories.items():
        print(f" -{cat}: {total:.2f}")
    print("-"*6)
    print("\nCategories Of The Income: ")
    for cat, total in income_categories.items():
        print(f" -{cat}: {total:.2f}")
    print("-"*6)