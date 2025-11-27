from models.account import Account
from models.transaction import Transaction
from models.category import Category
from utils.file_manager import import_previous_data, save_data_to_file
from utils.report import monthly_report
from models.password import create_password

#choose category for the transactions amount
def choose_category(data, c_type):
    if c_type == "income":
        categories = Category.Income_Categories
    elif c_type == "expense":
        categories = Category.Expense_Categories
    
    for i, cate in enumerate(categories, 1):
        print(f"{i} -> {cate}")

    category = int(input ("Choose Category for Your new amount: "))
    try:
        res = categories[category - 1]
    except:
        print("You Entered Invalid Category Number..")
    return res


data = import_previous_data()

def main():
    print ("\n** Personal Finance Manager **")

    while True:
        print("\n1. Login")
        print("2. Create New Account")
        print("3. Exit")

        choice = input ("Choose a Number From The List: ")
        if choice == '1':   # try to login
            username = input ("Enter Account Name: ")
            if not data["accounts"]:
                print("No accounts exist. Please create an account first.")
                continue
            for acc in data["accounts"]:
                    if (acc["name"]) == username:
                        # validate Password
                        password = input("Enter Your Password: ")
                        while (acc["password"] != password):
                            print ("Inncorrect Password.\nTry Again..")
                            password = input("Enter Your Password: ")

                        print("\n** Welcome Back **")
                        show_list(username, password)
                        break
                    else:
                        print(f"There Is No Account Named As {username}!")
                        break

        elif choice == '2':
            username = input ("Enter Account Name: ")
            while not username:
                print("Account Name is required.")
                username = input ("Enter Account Name: ")
            exists = False
            for acc in data["accounts"]:
                if (acc["name"]) == username:
                    print("This Account Already Exists.")
                    exists = True
                    break
            if exists == False:
                password = create_password()
                if password != '':
                    new_account = Account(username, password, 0)
                    data["accounts"].append(new_account.to_dict())
                    save_data_to_file(data)
                    print("Your New Account Created Successfully")
                    show_list(username, password)
                else:
                    continue
                
        elif choice == '3':
            print("Good Bye!")
            return 0
        
        else:
            print ("Please Select A Valid Number From The Lit (1-3)..\n")

        

def show_list(username, password):
    while True:
        print("*"*9)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Total Balance")
        print("4. show report for a month")
        print("5. Back")

        user_input = input ("Choose a Number From The List: ")


        if user_input == "1":
            exists = False
            while True:
                try:
                    amount = float(input("Enter New Amount to Add: "))
                    if amount <= 0:
                        print("The Amount Can't Be Negative or Zero!")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            for acc in data["accounts"]:
                if acc["name"] == username:
                    balance = acc["balance"]
                    new_acc = Account(username, password, balance)
                    try:
                        new_acc.add_balance(amount)
                    except ValueError as e:
                        print(e)
                        continue
                    acc["balance"] = new_acc.balance
                    exists = True
                    break
            if exists == False:
                print("Username is Wrong...\nPlease Try Another Name ...\n")
            
            category = choose_category(data, "income")
            note = input("Note: ")

            trans = Transaction("income", category, username, amount, note)
            data["transactions"].append(trans.to_dict())

            save_data_to_file(data)
            print(trans.__str__())
            print("New Income Added Successfully")


        elif user_input == "2":
            exists = False
            while True:
                try:
                    amount = float(input("Enter Amount to withdraw: "))
                    if amount <= 0:
                        print("The Amount Can't Be Negative or Zero!")
                        continue
                    for acc in data["accounts"]:
                        if acc["name"] == username:
                            balance = acc["balance"]
                            new_acc = Account(username, password, balance)
                            new_acc.reduce_balance(amount)
                            acc["balance"] = new_acc.balance
                            exists = True
                            break
                    if not exists:
                        print("Username is Wrong...\nPlease Try Another Name ...\n")
                    else:
                        break
                except ValueError as e:
                    print(e)
                except Exception:
                    print("Invalid input. Please enter a number.")

            category = choose_category(data, "expense")
            note = input("Note: ")
            trans = Transaction("expense", category, username, amount, note)
            data["transactions"].append(trans.to_dict())
            save_data_to_file(data)
            print(trans.__str__())
            print("New Expense Done Successfully")


        elif user_input == "3":
            exists = False
            while exists == False:
                for acc in data["accounts"]:
                    if acc["name"] == username:
                        balance = acc["balance"]
                        acc = Account(username, password, balance)
                        print(acc.__str__())
                        print("\n")
                        exists = True
                        break
                if exists == False:    
                        print ("Username is Wrong...\nPlease Try Another Name ...\n")

        elif user_input == "4":
            month = input ("Enter A Date YYYY-mm Like (2025-11): ")
            monthly_report(data, month, username)

        elif user_input == "5":
            print("Back To Main List!")
            break

        else:
            print ("Please Select A Valid Number From The Lit (1-5)..\n")

main()

# refactor: improve validation and structure for account, transactions, and user input
