# Programmer: Arash
# Date: 11-21-2026
# Purpose: Handle invalid input in the Name Game
# Instructor: Deodat Sharma

def trunc_name(name):  # Find the part of the name that starts at its first vowel
    name = name.strip().lower()
    for i, letter in enumerate(name):
        if letter in "aeiou":  # Remove the starting consonants but keep the first vowel
            return name[i:]
    return name


def name_game(name):  # Yield one song line at a time instead of returning the whole song
    name = name.strip()
    short_name = trunc_name(name)
    if len(name.replace(" ", "")) < 2:
        raise ValueError("Please enter a name with at least two letters")
    for word in name.split():
        if not word.isalpha():
            raise ValueError("Please use letters and spaces only")
    first_letter = name[0].lower()
    b_sound = "" if first_letter == "b" else "b"
    f_sound = "" if first_letter == "f" else "f"
    m_sound = "" if first_letter == "m" else "m"
    # Names starting with b, f, or m skip that letter on its matching song line.
    yield f"{name}, {name}, bo-{b_sound}{short_name}"
    yield f"banana fana fo-{f_sound}{short_name}"
    yield f"me my mo-{m_sound}{short_name}"
    yield f"{name}!"


while True:
    try:
        entered_name = input("Enter a name: ").strip()
        if entered_name.lower() in ["bart", "buck", "chuck"]:
            print("That name can make an inappropriate rhyme. Please choose another name.")
            continue
        for line in name_game(entered_name):  # Generator errors happen when the loop asks for a line
            print(line)
    except ValueError as error:
        print(error)
    else:
        break  # A valid name finishes the game instead of asking again

# An empty name would cause IndexError at name[0] in the original function without its input checks.
# A numeric name or a single letter may not raise an error by itself, so the length and letter checks raise ValueError.
# SystemExit(0) asks Python to stop the program with a success status. break only leaves the nearest loop.
# SystemExit can also end an interactive session, so it may stop more than expected inside a notebook.
