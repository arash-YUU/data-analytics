# Programmer: Arash
# Date: 11-15-2026
# Purpose: Use dictionaries to store and print an address
# Instructor: Deodat Sharma

contact_info = {
    "name": "Alex Morgan",
    "address": "123 Example Street",
    "city": "Sacramento",
    "state": "CA",
    "zip": "95814"
}

print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

del contact_info["name"]                 # Remove the original name

full_name = {
    "first name": "Alex",
    "last name": "Morgan"
}

full_name.update({"honorific": "Mx."})   # Add a title to the name
contact_info.update({"full_name": full_name})  # Add the name dictionary to the contact

print(f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")
