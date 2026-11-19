# Programmer: Arash
# Date: 11-18-2026
# Purpose: Store customer profiles in a restaurant rewards program
# Instructor: Deodat Sharma

cust_list = []  # This stays outside the class so adding a customer does not reset the list


class RewardsProgram:
    """Store a customer profile and add it to the shared customer list."""

    def __init__(self, cust_name, phone, email):  # Runs when a new customer profile is created
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):  # Print the details stored in this customer object
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):  # Use this customer's name in the thank-you message
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):  # Keep the customer details together as one tuple in the shared list
        cust_list.append((self.cust_name, self.phone, self.email))
        # append keeps the earlier customers instead of replacing them.


customer1 = RewardsProgram("Alex Morgan", "202-555-0101", "alex@example.com")
customer2 = RewardsProgram("Sam Lee", "202-555-0102", "sam@example.com")
customer3 = RewardsProgram("Jordan Kim", "202-555-0103", "jordan@example.com")

for customer in [customer1, customer2, customer3]:  # Run the methods for all three customers without resetting the shared list
    customer.profile()
    customer.thank_you()
    customer.add_to_cust_list()
    print()

print(cust_list)
