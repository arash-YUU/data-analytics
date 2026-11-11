# Programmer: Arash
# Date: 11-11-2026
# Purpose: Convert temperature from Fahrenheit to Celsius
# Instructor: Deodat Sharma

fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Get user input for temperature in Fahrenheit
celsius = (fahrenheit - 32) * 5 / 9                             # Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9

print(f"Temperature in Celsius is: {celsius:.2f}")              #Display the temperature in Celsius formatted to 2 decimal places
