# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate the distance between cordinates using sqrt function from math module
# Instructor: Deodat Sharma
from math import sqrt                                                   # Import the sqrt function from the math module to calculate the square root

x1 = float(input("Enter x-coordinate of first point: "))                # Get user input for x-coordinate of first point
y1 = float(input("Enter y-coordinate of first point: "))                # Get user input for y-coordinate of first point
x2 = float(input("Enter x-coordinate of second point: "))               # Get user input for x-coordinate of second point
y2 = float(input("Enter y-coordinate of second point: "))               # Get user input for y-coordinate of second point

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)                        # Calculate the distance between the two points using the distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)

print(f"The distance between the coordinates is: {distance:.2f}")       # Display the distance between the coordinates formatted to 2 decimal places