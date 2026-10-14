correct_username = "student"
correct_password = "python123"

user = input("Enter password: ")
password = input("Enter password: ")

if user == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Incorrect username or password")