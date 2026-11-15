# Programmer: Arash
# Date: 11-15-2026
# Purpose: Use tuples and a set to create candy options
# Instructor: Deodat Sharma

candy_types = ("Gummies", "Lollipops", "Jelly beans")
fruit_flavors = ("Strawberry", "Mango", "Watermelon")

candy_options = {
    fruit_flavors[0] + " " + candy_types[0],
    fruit_flavors[1] + " " + candy_types[1],
    fruit_flavors[2] + " " + candy_types[2]
}                                       # Make a set using items from both tuples

print("Today's candy options include:")
print(candy_options)
print(candy_options)
print(candy_options)

# The order stays the same in these prints, but it may change when I run the script again.
# A set does not keep items in a fixed order.
