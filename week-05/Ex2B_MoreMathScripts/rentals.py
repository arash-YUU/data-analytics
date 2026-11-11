# Programmer: Arash
# Date: 11-11-2026
# Purpose: Calculate number of vans, cost per van, and cost per person for a tour.
# Instructor: Deodat Sharma

people_going = int(input("Enter the number of people going: "))    # Get user input for the number of people going
van_capacity = 15                                                  # Set the van capacity to 15 people
van_cost = 250                                                     # Set the cost of the van to $250
vans_needed = people_going // van_capacity                         # Calculate the number of vans needed by performing integer division of the number of people going by the van capacity

if people_going % van_capacity != 0:                               # Check if there is a remainder when dividing the number of people going by the van capacity
    vans_needed += 1                                               # If there is a remainder, add 1 to the number of vans needed to account for the remaining people

print(f"Number of vans needed: {vans_needed}")                     # Display the number of vans needed
print(f"Total cost for vans: ${vans_needed * van_cost}")           # Display the total cost for the vans needed
print(f"Cost per person: ${round((vans_needed * van_cost) / people_going, 2)}")  # Display the cost per person by dividing the total cost for vans by the number of people going and rounding to 2 decimal places


#a) How much money did your script say you had to charge per person?
# Cost per person: $19.74

#b) If you multiply that out, how much did you collect?
# I get 750.12 but i used round fucntion to round it to nearest.

#c) How much were the vans?
# Total cost for vans: $750 

#d) Why do you have leftover money?
# Becasue i used rounf cuntion for cost per person, which make 19.7368 to 19.74 so each person pay alittle extra.