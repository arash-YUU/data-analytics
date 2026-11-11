# Programmer: Arash
# Date: 11-11-2026
# Purpose: Convert temperature from Celsius to Fahrenheit
# Instructor: Deodat Sharma

celsius = float(input("Enter temperature in Celsius: "))          # Get user input for temperature in Celsius
fahrenheit = (celsius * 9 / 5) + 32                               # Convert Celsius to Fahrenheit using the formula: (C * 9/5) + 32

print(f"Temperature in Fahrenheit is: {fahrenheit:.2f}")          # Display the temperature in Fahrenheit formatted to 2 decimal places