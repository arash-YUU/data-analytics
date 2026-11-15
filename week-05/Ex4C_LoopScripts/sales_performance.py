# Programmer: Arash
# Date: 11-15-2026
# Purpose: Print sales records and find top performers
# Instructor: Deodat Sharma

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

total_sales = 0

for name, region, sales in sales_data:  # Split each sales record into its three values
    print(f"{name} ({region}): ${sales:,.2f}")
    if sales > 5000:  # Exactly 5,000 does not count as a top performer
        print("  ^ Top performer!")
    total_sales = total_sales + sales  # Add each sale to the running total

print(f"Total sales: ${total_sales:,.2f}")
