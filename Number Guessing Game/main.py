import random

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20. Try to guess it!")

# Generate a random number
number_to_guess = random.randint(1, 20)
attempts = 0

# Game loop
while True:
    user_guess = input("Enter your guess: ")

    # Check if the input is a valid number
    if not user_guess.isdigit():
        print("Please enter a valid number!")
        continue

    user_guess = int(user_guess)
    attempts += 1

    # Provide feedback
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
