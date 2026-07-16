hours = float(input("Enter the number of hours worked:"))
rate = float(input("Enter the hourly pay rate"))

if hours<= 40:
    gross_pay = hours * rate
else:
    overtime = hours - 40
    gross_pay = (40*rate) + (overtime * rate * 1.5)

print(f"The gross pay is ${gross_pay:.2f}.")