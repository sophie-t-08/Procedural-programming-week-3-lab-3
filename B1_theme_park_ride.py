age = int(input("Enter your age: "))
height = float(input("Enter your height in cm as a decimal: "))
if age < 12:
    print("You are too young for this ride")
elif age >= 12 and height >= 140.0:
    print("You can ride")
else:
    print("You do not meet the requirements")