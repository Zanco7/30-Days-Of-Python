import random

#30-day Python challenge
print("------30-day Python challenge 2/30------")
print("Number Guessing Game")

max_attempts = 3
attempts = max_attempts

number = random.randint(1,20)

while True:
    try:
        guess = int(input("Guess the Number (1- 20)?: "))
    except ValueError:
        print("Error: please enter numbers only.\n")
        continue
    if guess < 1 or guess > 20:
        print("Please guess a number between 1 and 20.")
        continue

    if guess == number:
        used= max_attempts - attempts + 1
        print(f"Correct! 🎉 You guessed it in {used} tries.")
        break

    attempts -=1

    if attempts == 0:
        again = input("Game Over! Do you want to play again? (y/n): ").lower()
        if again == "y":
            number = random.randint(1, 20)
            attempts = max_attempts
            continue
        else:
            print("Goodbye! 👋")
            break

    elif guess < number:
        print("Too low!")
    else:
        print("Too High!")
