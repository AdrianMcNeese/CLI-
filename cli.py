import time 
import Customer 
import os 

Customer.load()
Customer.save()

cust = input("Hello, and welcome to CLI inc. Are you a new or returning customer? (Type 'new' or 'returning') \r\n>")
if cust == "new":       
        print("Welcome, new customer! CLI inc. is a data storage company geared towards keeping your information safe and secure.")
        time.sleep(1)
        Customer.add()
        print("Thank You for storing your information with CLI inc.! Have a great day!")
        time.sleep(2)
elif cust == "returning":
    nm = input("Welcome Back! What is your name? >")
    if Customer.has(nm):
        user = Customer.get(nm)
        choice = input("Would you like to \r\n1.View Customer Info \r\n2. Modify Customer \r\n3. Add/Use LoyaltyPoints \r\n4. View Customer List \r\n>")
        if choice == '1':
            print(user)
            time.sleep(2)
            print("Have a Great Day!")
            time.sleep(2)
            exit()
        elif choice == '2':
            edit = input("Would you like to: \r\n1. Change Customer Info \r\n2. Delete Customer \r\n>")  
            if edit == '1':
                Customer.replace(nm)
                Customer.save()
                print("Updating...")
                time.sleep(5)
                yn = input("Updated! Would you like to see? y/n\r\n>")
                if yn == "y":
                    Customer.viewpers(nm)
                    time.sleep(2)
                    print("Havee a great day!")
                    time.sleep(2)
                    exit()
                else:
                    print("Goodbye!")
                    exit()
            elif edit == '2':
                sel = input("Are you sure you would like to delete this customer? y/n \r\n>")
                if sel == "y":
                    Customer.delete(nm)
                    exit()
                elif sel == 'n':
                    print("Have a great day!")
                    time.sleep(1)
                    exit()
                else:
                    print("No choice made. Goodbye!")
                    exit()
            else:
                print("Sorry, that wasn't a choice")
                exit()
        elif choice == '3':
            point = input("Are you adding or using your LoyaltyPoints? \r\n 1.Adding \r\n 2.Using")
            if point == '1':
                Customer.addpoints(nm)
                Customer.save()
                print("Updating...")
                time.sleep(5)
                yn = input("Updated! Would you like to see? y/n\r\n>")
                if yn == "y":
                    Customer.viewpers(nm)
                    time.sleep(5)
                    print("Havee a great day!")
                    time.sleep(2)
                    exit()
            elif point == '2':
                Customer.takepoints(nm)
                Customer.save()
                print("Updating...")
                time.sleep(5)
                yn = input("Updated! Would you like to see? y/n\r\n>")
                if yn == "y":
                    Customer.viewpers(nm)
                    time.sleep(5)
                    print("Havee a great day!")
                    time.sleep(2)
                    exit()
            else:
                print("No choice made. Goodbye!")
                exit()  
        elif choice == '4':
            if Customer.isadmin(nm):
                Customer.view()
                time.sleep(5)
                print("Goodbye!")  
                time.sleep(2)
                exit()
            else:
                print("You do not have permission! Goodbye!")
                exit()           
        else: 
            print("No choice made. Goodbye!") 
            exit()  
    else:
        print("This name is not in our system. Sorry!")
        exit()
else:
    print("Incorrect input")
    exit()