# Programmer: Arash
# Date: 11-15-2026
# Purpose: Test changing strings to numbers, slicing, and removing spaces
# Instructor: Deodat Sharma

# Set the starting values
a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

print(a, type(a))                 # Show a and its type
print(b, type(b))                 # Show b and its type
print(c, type(c))                 # Show c and its type
print(d, type(d))                 # Show d and its type

# Change the strings to integers
#a_int = int(a)                   # ValueError because a has a decimal point
b_int = int(b)                    # Change b to an integer
#c_int = int(c)                   # ValueError because c has letters
#d_int = int(d)                   # ValueError because d has letters

print(b_int, type(b_int))         # Show the result and its type

# Change the strings to floats
a_float = float(a)               # Change a to a float
b_float = float(b)                # Change b to a float
#c_float = float(c)               # ValueError because c has letters
#d_float = float(d)               # ValueError because d has letters

print(a_float, type(a_float))     # Show the result and its type
print(b_float, type(b_float))     # Show the result and its type

# Change a to a float first, then to an integer
a_int = int(float(a))            # The result is 101 because int() drops the decimal part
print(a_int, type(a_int))         # Show the result and its type

# Get just the numbers using slicing
a_number = float(a[2:7])         # Get 101.1 and change it to a float
b_number = int(b[:2])             # Get 55 and change it to an integer
c_number = int(c[:3])             # Get 402 and change it to an integer
d_number = int(d[7:8])            # Get 5 and change it to an integer

print(a_number, type(a_number))   # Show the number and its type
print(b_number, type(b_number))   # Show the number and its type
print(c_number, type(c_number))   # Show the number and its type
print(d_number, type(d_number))   # Show the number and its type

# Remove spaces from both ends
print(a.strip())                  # Show 101.1 without extra spaces
print(d.strip())                  # Show Number 5 without extra spaces
