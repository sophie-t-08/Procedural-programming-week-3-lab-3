age = int(input("Enter your age: "))
order_total = float(input("Enter your order total (£): "))
account_status = input("Enter account status (yes or no): ")
valid_disc_code = input("Do you have a valid discount code? Enter yes or no: ")
account_status.lower()
valid_disc_code.lower()

if order_total <= 0:
    print("Invalid order total")

if account_status == "no":
    print("Please activate account")

if age < 18:
    parental_auth = input("Do you have parental authorisation? Enter yes or no: ")
    parental_auth.lower()
    if parental_auth == "yes" and order_total < 100:
        print("Order approved")
    elif parental_auth == "no" and order_total < 100:
        print("Please get parental authorisation")
    elif parental_auth == "yes" and order_total > 100:
        print("Order total above authorised value")
    