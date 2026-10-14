starting_balance = 1000
correct_pin = "1234"

enter_pin = input("Enter PIN: ")
if enter_pin != correct_pin:
    print("Incorrect pin")

if enter_pin == correct_pin:
    choice = input("Choose balance, withdraw or deposit? ")
    choice.lower()
    if choice == "balance":
        print(starting_balance)
    elif choice == "withdraw":
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount > starting_balance:
            print("Withdraw amount is higher than balance")
        elif withdraw_amount < 0:
            print("Withdraw amount is a negative number")
        elif withdraw_amount <= starting_balance and withdraw_amount > 0:
            current_balance = starting_balance - withdraw_amount
            print("Withdraw successful, current balance is now", current_balance)
    elif choice == "deposit":
        deposit_amount = int(input("Enter deposit value: "))
        if deposit_amount > 0:
            current_balance = starting_balance + deposit_amount
            print("Deposit successful, current balance is now", current_balance)
    else:
        print("Error, please try again")