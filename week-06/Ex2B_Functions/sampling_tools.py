# Programmer: Arash
# Date: 11-18-2026
# Purpose: Use random functions to sample a product inventory
# Instructor: Deodat Sharma

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

product_of_day = random.choice(products)  # choice picks one product from the list
survey_products = random.sample(products, 3)  # sample does not pick the same item twice
print(f"Product of the Day: {product_of_day}")
print(f"Products for the survey: {survey_products}")

random.shuffle(products)  # shuffle changes the list itself and returns None
print(f"Products in random order: {products}")

transaction_count = random.randint(50, 300)  # Both 50 and 300 are possible results
print(f"Daily transaction count: {transaction_count}")
