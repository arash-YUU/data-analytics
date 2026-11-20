# Programmer: Arash
# Date: 11-20-2026
# Purpose: Track restaurant customer counts and ratings
# Instructor: Deodat Sharma

class Restaurant:
    """Store restaurant details, customer counts, and ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):  # Add today's customers to the count already saved
        customers = input("How many customers served today? ").strip()
        while not customers.isdecimal():
            customers = input("Please enter a whole number of zero or more: ").strip()
        self.number_served += int(customers)

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):  # Keep asking until the rating is a whole number from 1 to 5
        rating = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ").strip()
        while rating not in ["1", "2", "3", "4", "5"]:
            rating = input("Please enter a whole number from 1 to 5: ").strip()
        self.customer_ratings.append(int(rating))
        average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
        # Include every saved rating when finding the new average.
        print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.2f}")


restaurant1 = Restaurant("Pasta Corner", "Italian food")
restaurant2 = Restaurant("Taco House", "Mexican food")
restaurant3 = Restaurant("Kabul Kitchen", "Afghan food")

for restaurant in [restaurant1, restaurant2, restaurant3]:
    restaurant.describe_rest()
    restaurant.rest_open()
    restaurant.print_num_served()
    for visit in range(2):  # Repeat the inputs to check that counts and ratings add up
        restaurant.add_num_served()
        restaurant.customer_rating()
    restaurant.print_num_served()
    print()
