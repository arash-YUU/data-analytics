# Programmer: Arash
# Date: 11-15-2026
# Purpose: Practice if and else statements
# Instructor: Deodat Sharma

x = 100
y = 20

if x / y == 5:
    print("x divided by y is 5")
    x = 1                             # Change x before the next check
else:
    print("are the variables set up correctly?")

if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print(f"Whoops, x equals {x}")

if x < y:
    print("x is less than y")
    x = x * 2                         # Double the value of x
else:
    print("uh oh, x is not less than y")

if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

print(f"The final value of x is {x} and the final value of y is {y}")
