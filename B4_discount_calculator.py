total = float(input("Enter the total cost of your shopping: "))
if total < 50:
    print("No discount")
elif total >= 50 and total < 100:
    discount = (total/100)*10
    total = total - discount
    print("10% discount applied, total is now", total)
elif total >= 100:
    discount = ((total/100)*10)*2
    total = total - discount
    print("20% discount applied, total is now", total)