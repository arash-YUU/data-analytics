# Programmer: Arash
# Date: 11-15-2026
# Purpose: Find a department name using match and case
# Instructor: Deodat Sharma

dept_code = 18                        # Set the department code to check

match dept_code:                      # Match the code with one of the cases below
    case 1:
        dept_name = "Marketing"
    case 5:
        dept_name = "Human Resources"
    case 10:
        dept_name = "Accounting"
    case 12:
        dept_name = "Legal"
    case 18:
        dept_name = "IT"
    case 20:
        dept_name = "Customer Relations"
    case _:
        dept_name = "Unknown department"  # Use this when no other case matches

print(f"Department code {dept_code} is {dept_name}")  # Show the code and department name
