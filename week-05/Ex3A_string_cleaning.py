# Programmer: Arash
# Date: 11-15-2026
# Purpose: Clean names and salary strings
# Instructor: Deodat Sharma

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())             # Change the name to lowercase
print(name_2.lower())
print(name_3.lower())

print(name_1.title())             # Start each word with a capital letter
print(name_2.title())
print(name_3.title())

salary_1_clean = salary_1.replace("$", "")   # Remove the dollar sign
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)
print(type(salary_1_clean))        # The cleaned value is still a string
print(type(salary_2_clean))

# Remove the comma and change the string to a number before doing math.
salary_1_number = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_number)             # Show 82500 as a number
print(type(salary_1_number))       # Confirm the result is an integer
