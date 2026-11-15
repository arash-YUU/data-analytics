# Programmer: Arash
# Date: 11-15-2026
# Purpose: Find a department name using its code
# Instructor: Deodat Sharma

dept_code = 18                        # Set the department code to check

if dept_code == 1:
    dept_name = "Marketing"
elif dept_code == 5:
    dept_name = "Human Resources"
elif dept_code == 10:
    dept_name = "Accounting"
elif dept_code == 12:
    dept_name = "Legal"
elif dept_code == 18:
    dept_name = "IT"
elif dept_code == 20:
    dept_name = "Customer Relations"
else:
    dept_name = "Unknown department"  # Use this when the code is not in the list

print(f"Department code {dept_code} is {dept_name}")  # Show the code and department name
