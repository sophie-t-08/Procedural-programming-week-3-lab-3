original_total = float(input("Enter the total cost of your shopping: "))
student = bool(input("Are you a student? Enter true if yes or false if no: "))
if original_total < 50:
    print("No discount")
    discount = 0
    final_total = original_total
elif original_total >= 50 and original_total < 100:
    discount = (original_total/100)*10
    final_total = original_total - discount
    print("10% discount applied, total is now", final_total)
elif original_total >= 100:
    discount = ((original_total/100)*10)*2
    final_total = original_total - discount
    print("20% discount applied, total is now", final_total)

print("Initial total: £",original_total)
print("Discount: £",discount)
print("Final total to pay: £",final_total)

if student == True and original_total >= 50:
    student_discount = ((original_total/100)*10)/2
    student_total = final_total - discount
    final_discount = discount + student_discount
    print("Student discount: £",student_discount)
    print("Initial total: £",original_total)
    print("Total discount: £",final_discount)
    print("Final total to pay: £",student_total)


if final_total < 0:
    print("Error, please re-enter total")