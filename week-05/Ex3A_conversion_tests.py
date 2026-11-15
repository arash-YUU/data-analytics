# Programmer: Arash
# Date: 11-15-2026
# Purpose: Test changing strings to numbers, slicing, and removing spaces
# Instructor: Deodat Sharma


a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


#a_int = int(a)                   # ValueError because a has a decimal point
b_int = int(b)
#c_int = int(c)                   # ValueError because c has letters
#d_int = int(d)                   # ValueError because d has letters

print(b_int, type(b_int))


a_float = float(a)
b_float = float(b)
#c_float = float(c)               # ValueError because c has letters
#d_float = float(d)               # ValueError because d has letters

print(a_float, type(a_float))
print(b_float, type(b_float))


a_int = int(float(a))  # float handles the decimal string first; int then drops the decimal part
print(a_int, type(a_int))


a_number = float(a[2:7])  # The slice includes index 2 through 6, not index 7
b_number = int(b[:2])
c_number = int(c[:3])
d_number = int(d[7:8])  # The digit is at index 7 after the word and space

print(a_number, type(a_number))
print(b_number, type(b_number))
print(c_number, type(c_number))
print(d_number, type(d_number))


print(a.strip())  # strip removes outside spaces but the result is still a string
print(d.strip())
