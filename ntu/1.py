hours_worked = int(input("Number of hours worked in a month: "))
overtime_limit = 160
basic_pay_rate = 10

if hours_worked > overtime_limit:
    overtime_pay = (hours_worked - overtime_limit) * 1.5 * basic_pay_rate
    gross_pay = overtime_limit * basic_pay_rate + overtime_pay
else:
    gross_pay = hours_worked * basic_pay_rate
print(f"gross pay: {gross_pay}")

amount_to_be_taxed = gross_pay
if amount_to_be_taxed >= 1000:
    tax = 1000 * 0.1
    amount_to_be_taxed -= 1000
    if amount_to_be_taxed >= 500:
        tax += 500 * 0.2
        amount_to_be_taxed -= 500
        tax += amount_to_be_taxed *0.3
else:
    tax = gross_pay * 0.1

print(f"tax: {tax}")

net_pay = gross_pay - tax
print(f"net pay: {net_pay}")