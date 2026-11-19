# Programmer: Arash
# Date: 11-18-2026
# Purpose: Create restaurant objects and call their methods
# Instructor: Deodat Sharma

class Restaurant:
    """Store a restaurant name and food type and display its information."""

    def __init__(self, rest_name, food_type):  # Runs when a new restaurant object is created
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):  # Uses this restaurant's details to describe its food
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):  # Prints the open message for this restaurant
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant("Pasta Corner", "Italian food")
restaurant2 = Restaurant("Taco House", "Mexican food")
restaurant3 = Restaurant("Kabul Kitchen", "Afghan food")

for restaurant in [restaurant1, restaurant2, restaurant3]:  # Run both methods for each restaurant
    restaurant.describe_rest()
    restaurant.rest_open()
