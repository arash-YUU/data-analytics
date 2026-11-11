# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate taxes withheld based on a monthly income and tax rate
# Instructor: Deodat Sharma

tax_rate = 0.23
monthly_income = 10000.678

taxes = monthly_income * tax_rate

print(f"Taxes withheld on a monthly income of ${round(monthly_income, 2):,}\
 at a tax rate of {int(tax_rate * 100)}% is ${round(taxes, 2):,.2f}")