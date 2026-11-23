# Programmer: Arash
# Date: 11-21-2026
# Purpose: Append a night-out description to a text file
# Instructor: Deodat Sharma

f = open("about_me.txt", "a")  # Append keeps the text already in the file
f.write("Perfect night out: Dinner with friends, a movie, and a walk by the water.\n")
f.close()
