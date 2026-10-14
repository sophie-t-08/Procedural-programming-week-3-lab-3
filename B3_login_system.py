correct_username = "student"
correct_password = "python123"

user = input("Enter username: ")
password = input("Enter password: ")

if user == correct_username and password == correct_password:
    print("Login successful")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access granted")
    else:
        print("You must be at least 18")
else:
    print("Incorrect username or password")

if user == correct_username and password != correct_password:
    print("Username recognised")