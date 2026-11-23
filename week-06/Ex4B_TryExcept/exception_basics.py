# Programmer: Arash
# Date: 11-21-2026
# Purpose: Handle common Python errors using try and except
# Instructor: Deodat Sharma

try:
    number = int("twelve")
except ValueError:
    print("ValueError: The text cannot be changed to an integer")
else:
    print(number)
finally:
    print("Let's try another one...")

try:
    total = missing_number + 5  # This name has not been defined
except NameError:
    print("NameError: The variable does not exist")
else:
    print(total)
finally:
    print("Let's try another one...")

try:
    total = "5" + 2
except TypeError:
    print("TypeError: A string and an integer cannot be added directly")
else:
    print(total)
finally:
    print("Let's try another one...")

try:
    result = eval("5 +")  # Parsing text inside try lets this example catch a syntax error
except SyntaxError:
    print("SyntaxError: The expression is missing a value after the plus sign")
else:
    print(result)
finally:
    print("Let's try another one...")

# A syntax mistake in the script itself stops Python before these try blocks can run.
# Other examples are ZeroDivisionError for 5 / 0 and IndexError for a list index that does not exist.
