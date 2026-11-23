# Programmer: Arash
# Date: 11-21-2026
# Purpose: Practice reading characters and lines from a text file
# Instructor: Deodat Sharma

f = open("about_me.txt", "r")

# print(f.read())
# print(f.read(50))
# print(f.read(50))  # The second read continues after the first 50 characters

# print(f.readline(10))
# print(f.readline())  # Reads the rest of the current line after the first 10 characters
# for i in range(1, 5):
#     print(f.readline())

# print(f.readlines(1))
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))  # A negative size reads all the remaining lines
# readlines uses the size as a hint and keeps whole lines, so it can return more characters.

first_50 = f.read(50)
next_four_lines = []
for i in range(1, 5):  # Continue from the current file position, not from the beginning
    next_four_lines.append(f.readline())
next_100 = f.readlines(100)
f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")
