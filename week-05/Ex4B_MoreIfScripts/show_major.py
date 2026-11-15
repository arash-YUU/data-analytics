# Programmer: Arash
# Date: 11-15-2026
# Purpose: Find a major and department office from a code
# Instructor: Deodat Sharma

student_name = "Alex Morgan"
student_major = "ENG"

if student_major == "BIOL":  # Each matching code gives the major name and its office
    major_name = "Biology"
    office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    office = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"  # No major in the table matched this code
    office = ""

print(f"Student: {student_name}")
print(f"Major: {major_name}")
if office:  # Skip the office line when the office is an empty string
    print(f"Department office: {office}")
