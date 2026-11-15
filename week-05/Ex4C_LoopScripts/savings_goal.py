# Programmer: Arash
# Date: 11-15-2026
# Purpose: Use a while loop to reach a savings goal
# Instructor: Deodat Sharma

bank_balance = 100
savings_goal = 500
weekly_savings = 50
treat_cost = 5

if weekly_savings <= treat_cost or treat_cost < 0:  # Savings must still grow after paying for a treat
    raise ValueError("Weekly savings must be greater than the treat cost, and the treat cost cannot be negative")

while bank_balance < savings_goal:  # Keep adding weekly savings until the goal is reached
    bank_balance = bank_balance + weekly_savings

    if bank_balance >= savings_goal * 0.75:  # Check 75 percent first because it is also more than halfway
        bank_balance = bank_balance - treat_cost  # The treat comes out of the savings balance
        print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}.")
    elif bank_balance > savings_goal / 2:  # This message applies above halfway but below 75 percent
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}.")
    else:
        print(f"This week my balance increased to ${bank_balance:.2f}.")

print(f"Goal met! My current balance is ${bank_balance:.2f}.")
