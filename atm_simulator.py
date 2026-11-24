balance = 5000
pin = 1234
Enter_pin = int(input("Enter Your pin:"))

if Enter_pin == pin:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            print("Your Balance:",balance)
        
        elif choice == 2:
            withdraw = int(input("Enter Your Amount:"))
            if balance >= withdraw:
                print("Withdraw Successful")
                balance -= withdraw
                print("Your Balance:",balance)
            else:
                print("Insufficient balance")
           
        elif choice == 3:
            deposit = int(input("Enter Deposit Amount:"))
            balance += deposit
            print("Your Balance:", balance)

        elif choice == 4:
            print("Thank you for using this ATM")
            break
else:
    print("Incorrect Pin")