from models.account import account
from models.transaction import Transaction
from models.category import Category
from utils.file_manager import import_previous_data, save_data_to_file
from utils.report import monthly_report

#choose category for the transactions amount
def choose_category(data, c_type):
    if c_type == "income":
        categories = Category.Income_Categories
    elif c_type == "expense":
        categories = Category.Category_names
    
    for i, cate in enumerate(categories, 1):
        print(f"{i} -> {cate}")

    category = int(input ("Choose Category for Your new amount: "))
    try:
        res = categories[category - 1]
    except:
        print("You Entered Invalid Category Number..")
    return res



def main():
    print ("\n** Personal Finance Manager **")
    data = import_previous_data()
    
    while True:
        print("*"*9)
        print("1. Create New Account")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Show Total Balance")
        # print("5. edit categories")
        print("5. show report for a month")
        print("6. Exit")

        user_input = input ("Choose a Number From The List: ")

        if user_input == "1":
            exists = False
            username = input ("Enter Account Name: ")
            for acc in data["accounts"]:
                if (acc["name"]) == username:
                    print("This Account Already Exists.")
                    exists = True
                    break
            if exists == False:
                balance = float(input ("Enter Your Balance: "))
                new_account = account(username, balance)
                data["accounts"].append(new_account.to_dict())
                save_data_to_file(data)
                print("Your New Account Created Successfully")

        elif user_input == "2":
            exists = False
            amount = float(input("Enter New Amount to Add: "))

            
            while exists == False:
                username = input("Enter Account Name: ")
                for acc in data["accounts"]:
                    if acc["name"] == username:
                        balance = acc["balance"]
                        new_acc = account(username, balance)
                        new_acc.add_balance(amount)
                        acc["balance"] = new_acc.balance
                        exists = True
                        break
                if exists == False:    
                    print ("Username is Wrong...\nPlease Try Another Name ...\n")
            
            #categories
            category = choose_category(data, "income")
            #note
            note = input("Note: ")

            trans = Transaction("income", category, username, amount, note)

            data["transactions"].append(trans.to_dict())


            save_data_to_file(data)
            print (trans.__str__())
            print ("New Income Added Successfully")

        elif user_input == "3":
            exists = False
            amount = float(input("Enter Amount to withdraw: "))

            while exists == False:
                username = input("Enter Account Name: ")
                for acc in data["accounts"]:
                    if acc["name"] == username:
                        if amount < acc["balance"]:
                            acc["balance"] -= amount
                            exists = True
                            break
                        else:
                            print("This Amount Does Not Exists In Your Account..\n")
                            exists = True
                            break
                if exists == False:    
                    print ("Username is Wrong...\nPlease Try Another Name ...\n")
            
            #category
            category = choose_category(data, "expense")
            #note
            note = input("Note: ")

            trans = Transaction("expense", category, username, amount, note)

            data["transactions"].append(trans.to_dict())

            save_data_to_file(data)
            print (trans.__str__())
            print ("New Expense Done Successfully")

        elif user_input == "4":
            exists = False
            while exists == False:
                username = input("\nEnter Your Account Name: ")

                for acc in data["accounts"]:
                    if acc["name"] == username:
                        balance = acc["balance"]
                        acc = account(username,balance)
                        acc.__str__()
                        print("\n")
                        exists = True
                        break
                if exists == False:    
                        print ("Username is Wrong...\nPlease Try Another Name ...\n")

        elif user_input == "5":
            month = input ("Enter A Date YYYY-mm Like (2025-11): ")
            monthly_report(data, month, username)

        elif user_input == "6":
            print("Good Bye!")
            return 0

        else:
            print ("Please Select A Valid Number From The Lit (1-5)..\n")

main()