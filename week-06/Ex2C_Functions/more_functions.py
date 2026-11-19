# Programmer: Arash
# Date: 11-18-2026
# Purpose: Create mailing labels, add numbers, and display receipts
# Instructor: Deodat Sharma

def display_mailing_label(name, address, city, state, zip):  # Put the name, street, and city details on separate lines
    print(f"{name}\n{address}\n{city}, {state} {zip}")


def add_numbers(*numbers):  # The star collects any number of arguments into a tuple
    total = sum(numbers)
    expression = " + ".join(str(number) for number in numbers)  # Turn each number into text before joining them with plus signs
    print(f"{expression} = {total}")


def display_receipt(total_due, amount_paid):  # Compare the payment with the bill to find change or money still owed
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}\n")
    if amount_paid < total_due:  # Underpayment means there is still a balance, not change
        print(f"Remaining Balance: ${total_due - amount_paid:.2f}")
    else:
        print(f"Change Due: ${amount_paid - total_due:.2f}")


display_mailing_label("Alex Morgan", "123 Example Street", "Sacramento", "CA", "95814")
print()
display_mailing_label("Sam Lee", "456 Sample Avenue", "Oakland", "CA", "94612")
print()
add_numbers(5)
add_numbers(5, 8)
add_numbers(5, 8, 12, 20)
print()
display_receipt(25.50, 30.00)
print()
display_receipt(25.50, 25.50)
print()
display_receipt(25.50, 20.00)
