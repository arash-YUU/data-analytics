# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate the total cost of a meal including tax and tip
# Instructor: Deodat Sharma

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the total cost of the meal
total_cost = food_cost + tax + tip

# Display the results
# print("The total due is $" + str(total_cost))  # The str() function is used to convert the total_cost from a float to a string so it can be concatenated with the other strings in the print statement.

print("Food cost is $" + str(food_cost) + " and tax is $" + str(tax))  # Display the food cost
#print("Tip is $" + str(tip))  # Display the tip
print("Tip is $" + format(tip, ".2f"))  # Display the tip
print("The total due is $" + str(total_cost))  # Display the total cost of the meal