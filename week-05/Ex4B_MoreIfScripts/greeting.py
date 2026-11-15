# Programmer: Arash
# Date: 11-15-2026
# Purpose: Display a greeting based on the hour
# Instructor: Deodat Sharma

current_hour = 18                         # Set an hour from 0 to 23

if current_hour < 0 or current_hour > 23:
    print("Enter an hour from 0 to 23")
else:
    if current_hour < 10:
        print("Good morning!")
    elif current_hour < 17:
        print("Good day!")
    else:
        print("Good evening!")

    if current_hour >= 23 or current_hour < 4:  # Check the hours across midnight
        print("What are you doing up so late??")
