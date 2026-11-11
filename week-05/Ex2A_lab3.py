# Programmer: Arash
# Date: 11-11-2026
# Purpose: Using input() function to get user to enter values
# Instructor: Deodat Sharma

from math import pi

bank_balance = float(input("Enter your bank balance: "))
print(f"Your bank balance is ${bank_balance:,.2f}")

# Using input() funtion to calculate the circle area based on user input

radius =float(input("Enter the radius of the circel: "))
area = pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}")