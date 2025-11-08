from models.account import account
from models.transaction import Transaction
from utils.file_manager import import_previous_data, save_data_to_file

def main():
    print ("\n** Personal Finance Manager **")
    data = import_previous_data()
    
    while True:
        print("*"*9)
        print("1. Create New Account")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Show Total Balance")
        print("5. Exit")

        user_input = input ("Choose a Number From The List: ")

        if user_input == "1":
            username = input ("Enter Account Name: ")
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
                        acc = account(username, balance)
                        acc.add_balance(amount)
                        exists = True
                        break
                if exists == False:    
                    print ("Username is Wrong...\nPlease Try Another Name ...\n")
            
            # category = input ("Choose Category for Your new amount: ")
            note = input("Note: ")

            trans = Transaction("expense", username, amount, note)

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
            
            # category = input ("Choose Category for Your new amount: ")
            note = input("Note: ")

            trans = Transaction("income", username, amount, note)

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
            print("Good Bye!")
            return 0

        else:
            print ("Please Select A Valid Number From The Lit (1-5)..\n")

main()