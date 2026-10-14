num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operation: ")

if operator == "+":
    total = num1 + num2
    print(total)
elif operator == "-":
    total = num1 - num2
    print(total)
elif operator == "*":
    total = num1 * num2
    print(total)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        total = num1 / num2
        print(total)
elif operator == "%":
    total = num1 % num2
    print(total)
elif operator == ">":
    if num1 > num2:
        print(num1)
    else:
        print(num2)
elif operator == "<":
    if num1 < num2:
        print(num1)
    else:
        print(num2)
elif operator == ">=":
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    elif num1 == num2:
        print(num1, "is equal to", num2)
elif operator == "<=":
    if num1 < num2:
        print(num1)
    elif num2 < num1:
        print(num2)
    elif num1 == num2:
        print(num1, "is equal to", num2)
else:
    print("Invalid operator")