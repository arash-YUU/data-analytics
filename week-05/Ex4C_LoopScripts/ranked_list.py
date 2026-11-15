# Programmer: Arash
# Date: 11-15-2026
# Purpose: Print a numbered list using enumerate
# Instructor: Deodat Sharma

skills_to_learn = ["Python", "SQL", "Excel", "Tableau", "Power BI"]

for index, skill in enumerate(skills_to_learn, start=1):  # enumerate gives each skill a number starting at 1
    if index == 1:  # Only the first skill gets the top pick label
        print(f"{index}. {skill}  <- top pick!")
    else:
        print(f"{index}. {skill}")

print("Reverse order:")
for index, skill in enumerate(reversed(skills_to_learn), start=1):  # Read the list backward but start numbering at 1 again
    print(f"{index}. {skill}")
