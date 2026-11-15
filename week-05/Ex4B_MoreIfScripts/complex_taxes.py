# Programmer: Arash
# Date: 11-15-2026
# Purpose: Calculate weekly tax using the lab tax tables
# Instructor: Deodat Sharma

pay_rate = 17.30
hours_worked = 45
filing_status = "single"

if hours_worked > 40:  # Only hours above 40 get overtime pay
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime pays one and a half times the normal rate
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

annual_gross_pay = gross_pay * 52  # There are 52 weeks in a year


if filing_status == "single":  # Single and joint filers have different rates in the workbook
    if annual_gross_pay < 12000:  # Check the lowest income range first
        tax_rate = 0.05
    elif annual_gross_pay < 25000:  # The earlier check already ruled out income below 12,000
        tax_rate = 0.10
    elif annual_gross_pay < 75000:  # This range starts at 25,000 and ends below 75,000
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross_pay < 12000:  # Check the lowest income range first
        tax_rate = 0
    elif annual_gross_pay < 25000:  # The earlier check already ruled out income below 12,000
        tax_rate = 0.06
    elif annual_gross_pay < 75000:  # This range starts at 25,000 and ends below 75,000
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    raise ValueError("Filing status must be single or joint")

weekly_tax = round(gross_pay * tax_rate, 2)  # Use the workbook rate for weekly pay and round to cents
net_pay = gross_pay - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your estimated annual gross pay is ${annual_gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")
