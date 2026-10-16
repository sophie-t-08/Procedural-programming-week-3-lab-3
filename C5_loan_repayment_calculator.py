loan_amount = float(input("Enter loan amount in £: "))
annual_interest_rate = float(input("Enter annual interest rate in %: "))
repayment_years = float(input("Enter years to repay loan: "))
total_repaid = float(input("Enter how much has been repaid in £: "))

total_to_pay = loan_amount - total_repaid

monthly_interest_rate = (annual_interest_rate / 100) / 12
num_of_monthly_payments = repayment_years * 12

if loan_amount or repayment_years <= 0 or total_repaid == loan_amount:
    print("Invalid input")

if annual_interest_rate == 0:
    monthly_payment = total_to_pay / num_of_monthly_payments
    monthly_payment = round(monthly_payment, 2)
else:
    monthly_payment = total_to_pay * monthly_interest_rate * ((1 + monthly_interest_rate)**num_of_monthly_payments/((1 + monthly_interest_rate)**num_of_monthly_payments - 1))
    monthly_payment = round(monthly_payment, 2)

if monthly_payment > 500:
    print("Warning, your monthly payments are high")

years_to_pay = round((loan_amount / monthly_payment)/12, 2)
total_interest = years_to_pay * annual_interest_rate

print("Monthly payment: £",monthly_payment)
print("Total amount repaid: £",total_repaid)
print("Total interest: ",total_interest,"%")