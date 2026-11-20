# Programmer: Arash
# Date: 11-20-2026
# Purpose: Track restaurant visits and rewards points for each customer
# Instructor: Deodat Sharma

cust_list = []


class RewardsProgram:
    """Store a customer profile and reward points for each restaurant visited."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}  # The challenge uses a separate points balance for each restaurant

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    def calculate_rewards(self, food_bill):
        return int(food_bill)  # For a positive bill, int drops the cents and rounds points down

    def visit_rest(self):
        restaurant = input("Name of restaurant: ").strip()
        while not restaurant:
            restaurant = input("Please enter a restaurant name: ").strip()
        food_bill = float(input("What was the total food bill for this visit? "))
        while food_bill < 0:
            food_bill = float(input("Please enter a bill of zero or more: "))

        if restaurant not in self.restaurants_visited:  # Keep one entry for each restaurant
            self.restaurants_visited.append(restaurant)
            self.rewards_points[restaurant] = 0

        points = self.calculate_rewards(food_bill)
        self.rewards_points[restaurant] += points  # Returning to a restaurant adds to its earlier balance
        total_points = sum(self.rewards_points.values())
        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned: {total_points}")
        print(f"Points at {restaurant}: {self.rewards_points[restaurant]}")
        print(f"Thank you for visiting {restaurant}!")


customer1 = RewardsProgram("Alex Morgan", "202-555-0101", "alex@example.com")
customer2 = RewardsProgram("Sam Lee", "202-555-0102", "sam@example.com")
customer3 = RewardsProgram("Jordan Kim", "202-555-0103", "jordan@example.com")

for customer in [customer1, customer2, customer3]:
    customer.profile()
    customer.thank_you()
    customer.add_to_cust_list()

for visit in range(3):  # Repeated visits show how one customer's balances build up
    customer1.visit_rest()

print(f"Restaurants visited: {customer1.restaurants_visited}")
print(f"Points by restaurant: {customer1.rewards_points}")
print(cust_list)
