#simple atm simulator
#starting balance
balance = 10000
while True:
#menu
    print("ATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))
#opt1 - check balance
    if choice == 1:
        print("Current balance: ₹", balance)
#opt2 - deposit money
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)
#opt3 - withdraw money
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
#check if enough balance is there
        if amount > balance:
            print("Insufficient balance!")
#check minimum balance 
        elif balance - amount < 500:
            print("Minimum balance of ₹500 must remain!")

        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)
#opt4 - exit program
    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")