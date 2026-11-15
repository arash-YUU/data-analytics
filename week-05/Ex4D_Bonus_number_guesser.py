# Programmer: Arash
# Date: 11-15-2026
# Purpose: Make a number guessing game using collections
# Instructor: Deodat Sharma

number_pool = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
numbers = list(number_pool)  # Set order can change between runs, so the first number can change too
secret_number = int(numbers[0])
guessed_numbers = []

print("Guess a whole number from 1 to 10")

while True:
    answer = input("Enter your guess: ").strip()
    if not answer.isdecimal():  # Reject letters and empty answers before using int()
        print("Please enter a whole number from 1 to 10")
        continue

    guess = int(answer)
    if guess < 1 or guess > 10:  # Reject guesses outside the game range
        print("Your guess must be from 1 to 10")
        continue

    guessed_numbers.append(guess)  # Only valid guesses count toward the total
    if guess < secret_number:  # The player needs a larger number
        print("Higher")
    elif guess > secret_number:  # The player needs a smaller number
        print("Lower")
    else:
        print("You guessed it!")
        break  # A correct guess ends the loop

print(f"Number of guesses: {len(guessed_numbers)}")
print(f"Your guesses: {guessed_numbers}")
if len(guessed_numbers) < 5:  # The extra message is only for fewer than five guesses
    print("You're awesome!")
