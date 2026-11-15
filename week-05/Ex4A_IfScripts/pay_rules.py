# Programmer: Arash
# Date: 11-15-2026
# Purpose: Calculate gross pay with overtime
# Instructor: Deodat Sharma

pay_rate = 17.30                               # Pay for one hour
hours_worked = 45                              # Total hours worked

if hours_worked > 40:                          # Check if there is overtime
    regular_pay = pay_rate * 40                # Pay for the first 40 hours
    overtime_hours = hours_worked - 40          # Get the hours over 40
    overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime pays 1.5 times the normal rate
    gross_pay = regular_pay + overtime_pay     # Add regular pay and overtime pay
else:
    gross_pay = pay_rate * hours_worked        # Normal pay when there is no overtime

print(f"You worked {hours_worked} hours at ${pay_rate:.2f} per hour")
print(f"Your gross pay is ${gross_pay:.2f}")     # Show the pay with two decimal places
