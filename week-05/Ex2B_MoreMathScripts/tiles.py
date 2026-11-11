# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate the number of tiles needed to cover a room based on user input for length and width, 
#including extra tiles for breakage and cutting, and calculate the number of boxes needed based on the number of tiles per box
# Instructor: Deodat Sharma

from shutil import which


length = float(input("Enter the length of the room in feet: "))                 # Get user input for length of the room
width = float(input("Enter the width of the room in feet: "))                   # Get user input for width of the room     

area = length * width                                                           # Calculate the area of the room in square feet
tiles_needed = area                                                             # Calculate the number of tiles needed based on the area of the room,each tile covers 1 square foot
extra_tiles = tiles_needed * 0.10                                               # calculate the number of extra tiles needed to account for breakage and cutting,which is 10% of the total tiles needed
tiles_needed += extra_tiles                                                     # add the extra tiles to the total number of tiles needed
boxes_needed = tiles_needed / 12                                                # Calculate the number of boxes needed, since there are 12 tiles per box  

print(f"Total area of the room is: {area:.2f} square feet")                     # Display the total area of the room formatted to 2 decimal places
print(f"Total number of tiles needed (including 10% extra for breakage and cutting): {round(tiles_needed)}")  # Display the total number of tiles needed 
print(f"Total number of boxes needed: {round(boxes_needed)}")                   # Display the total number of boxes needed  