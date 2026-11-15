# Programmer: Arash
# Date: 11-15-2026
# Purpose: Find the smallest and largest of three numbers
# Instructor: Deodat Sharma

a = 15
b = 8
c = 23

smallest = a
largest = a

if b < smallest:  # Keep b if it is smaller than the value saved so far
    smallest = b
if c < smallest:  # Compare c with the smaller of a and b
    smallest = c

if b > largest:  # Keep b if it is larger than the value saved so far
    largest = b
if c > largest:  # Compare c with the larger of a and b
    largest = c

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
