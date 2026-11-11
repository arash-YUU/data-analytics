# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate how long it will take to double an investment using the Rule of 72
# Instructor: Deodat Sharma

#Question: What is the Rule of 72?
#Answer: The Rule of 72 is a simple way to estimate how long it will take for an investment to double in value, 
# given a fixed annual rate of interest. The rule states that you can divide 72 by the annual interest rate to get
# an approximate number of years it will take for the investment to double.

savings = 1000                                              # Current savings
interest_rate = 0.05                                        # Annual interest rate
time_to_double = 72 / (interest_rate * 100)                 # Time to double investment using the Rule of 72
years_to_double = int(time_to_double)                       # Convert time to double to an integer for display purposes

print(f"Your current savings is ${savings:,.2f}")
print(f"At an interest rate of {interest_rate * 100:.2f}%, your savings will be worth ${savings * 2:,.2f} in {years_to_double} years.")

# User input for savings and interest rate, below program will calculate the time to double the investment based on user input.
#savings = float(input("Enter your current savings: "))
 #interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
 # time_to_double = 72 / (interest_rate * 100)
 # years_to_double = int(time_to_double)

#print(f"Your current savings is ${savings:,.2f}")
#print(f"At an interest rate of {interest_rate * 100:.2f}%, your savings will be worth ${savings * 2:,.2f} in {years_to_double} years.")`