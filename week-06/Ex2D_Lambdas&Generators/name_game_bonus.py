# Programmer: Arash
# Date: 11-18-2026
# Purpose: Use a generator to print the Name Game
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
    first_letter = name[0].lower()
    b_sound = "" if first_letter == "b" else "b"
    f_sound = "" if first_letter == "f" else "f"
    m_sound = "" if first_letter == "m" else "m"
    # Names starting with b, f, or m skip that letter on its matching song line.
    yield f"{name}, {name}, bo-{b_sound}{short_name}"
    yield f"banana fana fo-{f_sound}{short_name}"
    yield f"me my mo-{m_sound}{short_name}"
    yield f"{name}!"


entered_name = input("Enter a name: ").strip()
while not entered_name or not all(word.isalpha() for word in entered_name.split()):  # Ask again if the name is empty or contains numbers or symbols
    entered_name = input("Please enter a name using letters and spaces: ").strip()

# print(trunc_name(entered_name))
for name in [entered_name, "Arash", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]:
    if name.lower() in ["bart", "buck", "chuck"]:  # Skip these names so their rhymes are not printed
        print(f"Skipping {name} because the rhyme may be inappropriate.")
        continue
    for line in name_game(name):  # Each yield supplies the next line of the song
        print(line)
    print()

# A multiword name keeps its later words in the rhyme. Capitalization does not change the vowel check.
