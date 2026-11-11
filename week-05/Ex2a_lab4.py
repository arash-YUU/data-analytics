# Programmer: Arash
# Date: 11-11-2026
# Purpose: Use f-strings and input() to calculate the total cost of a meal including tax and tip
# Instructor: Deodat Sharma

# Get input from the user
food_cost = float(input("Enter the cost of the food: "))
tax_percent = float(input("Enter the tax percentage: "))
tip = float(input("Enter the tip amount: "))

# Calculate the total cost of the meal and tax
tax = food_cost * tax_percent / 100
total_cost = food_cost + tax + tip

print(f"Food cost is ${food_cost:.2f} and tax is ${tax:.2f}")    # Display the food cost
print(f"Tip is ${tip:.2f}")                                      # Display the tip
print(f"The total due is ${total_cost:.2f}")                     # Display the total cost of the meal