# Programmer: Arash
# Date: 11-15-2026
# Purpose: Create a movie list and practice sorting and adding items
# Instructor: Deodat Sharma

movies_to_watch = ["Interstellar", "The Dark Knight", "Inception"]

print(f"The list movies_to_watch includes the {len(movies_to_watch)} movies I'd like to watch")
print(movies_to_watch)

print(sorted(movies_to_watch))     # Show the movies in alphabetical order
print(movies_to_watch)             # The original list stays in the same order

movies_to_watch.sort()             # Change the original list to alphabetical order
print(movies_to_watch)

movies_to_watch.append("The Matrix")  # Add another movie to the list
print(f"The list movies_to_watch includes the {len(movies_to_watch)} movies I'd like to watch")
print(movies_to_watch)
