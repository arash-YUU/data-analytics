# Programmer: Arash
# Date: 11-15-2026
# Purpose: Clean names and salary strings
# Instructor: Deodat Sharma

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print(name_1.title())  # title capitalizes each word, so LaTonya becomes Latonya
print(name_2.title())
print(name_3.title())

salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)
print(type(salary_1_clean))  # Removing a dollar sign does not change a string into a number
print(type(salary_2_clean))


salary_1_number = int(salary_1.replace("$", "").replace(",", ""))  # Both the dollar sign and comma must be removed before int() works

print(salary_1_number)
print(type(salary_1_number))
