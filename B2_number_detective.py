integer = int(input("Enter an integer: "))
if integer > 0:
    print("Positive")
    even_or_odd = integer%2
    if even_or_odd == 0:
        print("Even")
    else:
        print("Odd")
    if integer > 100:
        print("That's a large number")
elif integer == 0:
    print("Zero")
else:
    print("Negative")
