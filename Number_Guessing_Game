#Number Guessing Game
import random

def number_guessing_game():
    secret = random.randint(1, 20)  
    attempts = 0

    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 20")

    while True:   # loop until guessed correctly
        guess = int(input("Enter your guess: "))
        attempts += 1

        # control statements
        if guess == secret:
            print("🎉 Correct! You guessed it in", attempts, "attempts.")
            break  # exit loop when correct
        elif guess < secret:
            print("Too low! Try again.")
            continue  # skip rest and ask again
        else:
            print("Too high! Try again.")
            continue

    print("Game Over!")

# run the game
number_guessing_game()
