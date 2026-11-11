# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate the net worth of a person based on their assets and debts
# Instructor: Deodat Sharma

saving_account = 25000
vehicle = 12000
investments = 3000
credit_card_debt = 5000
vehicle_loan = 8000


total_assets = (saving_account + vehicle + investments)
total_debts = (credit_card_debt + vehicle_loan)
net_worth = total_assets - total_debts

print(f"Your total assets are ${total_assets:,}")
print(f"Your total debts are ${total_debts:,}")
print(f"Your net worth is ${net_worth:,}")
