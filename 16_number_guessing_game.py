#number guessing game
import random

best_score = 0  # storing minimum attempts used

while True:
    number = random.randint(1, 100)
    attempts = 7
    used = 0

    print("Guess the number between 1 and 100")
    print("You have 7 attempts")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        used = used + 1

        if guess == number:
            print("Correct You guessed it in", used, "attempts")

# updating best score
            if best_score is None or used < best_score:
                best_score = used
                print("New Best Score:", best_score)

            break

        elif guess > number:
            print("Too high")

        else:
            print("Too low")

# bonus hint (within 5 difference)
        if abs(guess - number) <= 5:
            print("Hint: You are very close")

        attempts = attempts - 1
        print("Attempts remaining:", attempts)

    if attempts == 0 and guess != number:
        print("You failed The number was:", number)

# asking to play again
    again = input("Do you want to play again (yes/no): ")

    if again.lower() != "yes":
        print("Game Over")
        break