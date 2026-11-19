# Programmer: Arash
# Date: 11-18-2026
# Purpose: Use lambdas to create multiplier functions
# Instructor: Deodat Sharma

doubler = lambda n: n * 2
tripler = lambda n: n * 3

for value in [8, -4, 'banana']:  # Try the same lambdas with positive, negative, and text values
    print(f"Double {value}: {doubler(value)}")
    print(f"Triple {value}: {tripler(value)}")
    # Multiplying a string repeats the text instead of doing numeric math.


def multiplier(times):  # Create a new function that multiplies by the chosen amount
    return lambda n: n * times  # The returned function keeps the chosen multiplier


quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(f"4 times 8: {quadrupler(8)}")
print(f"5 times 8: {quintupler(8)}")
print(f"6 times 8: {sextupler(8)}")
print(f"7 times 8: {septupler(8)}")
print(f"8 times 8: {octupler(8)}")
print(f"9 times 8: {nonupler(8)}")
print(f"10 times 8: {decupler(8)}")
