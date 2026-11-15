# Programmer: Arash
# Date: 11-15-2026
# Purpose: Check whether a year is a leap year
# Instructor: Deodat Sharma

year = 2000

if year % 400 == 0:  # A year divisible by 400 is a leap year, including 2000
    leap_year = True
elif year % 100 == 0:  # Other century years are not leap years, including 1900
    leap_year = False
elif year % 4 == 0:  # For the remaining years, divisibility by 4 decides the result
    leap_year = True
else:
    leap_year = False

if leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
