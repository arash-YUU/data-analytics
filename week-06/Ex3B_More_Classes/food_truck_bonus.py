# Programmer: Arash
# Date: 11-20-2026
# Purpose: Use inheritance to track a food truck and its locations
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

for restaurant in [restaurant1, restaurant2, restaurant3]:
    restaurant.describe_rest()
    restaurant.rest_open()


class FoodTruck(Restaurant):
    """Add private bookings, a current location, and location history to a restaurant."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)  # Let Restaurant save the shared name and food details
        self.private_bookings = "N"
        self.truck_location = ""
        self.location_history = []

    def accepts_private_bookings(self):
        bookings = input("Does this food truck accept private bookings? Y/N ").strip().upper()
        while bookings not in ["Y", "N"]:
            bookings = input("Please enter Y or N: ").strip().upper()
        self.private_bookings = bookings
        if self.private_bookings == "Y":
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck currently does not accept private bookings.")

    def relocate_truck(self):
        location = input("Enter the truck's current location (street address and city): ").strip()
        while not location:
            location = input("Please enter the street address and city: ").strip()
        self.truck_location = location
        self.location_history.append(location)
        # Keep repeat locations to show the order of stops, including return visits.
        # Dates and times could also help show when each visit happened.
        print(f"Truck is currently located at {self.truck_location}")


truck1 = FoodTruck("Taco Wheels", "Mexican food")
truck1.describe_rest()  # The child class can use the parent class methods
truck1.rest_open()
truck1.accepts_private_bookings()
for stop in range(3):
    truck1.relocate_truck()
print(f"Location history: {truck1.location_history}")
