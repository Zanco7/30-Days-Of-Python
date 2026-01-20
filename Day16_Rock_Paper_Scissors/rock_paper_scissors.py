import random

# 30-day Python challenge
print("------30-day Python challenge 16/30------")
print("Rock ✊ Paper ✋ Scissors ✌️")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

running = True

while running:
    user_choice = input(
        "\nChoose rock, paper, or scissors (or q to quit): "
    ).strip().lower()

    if user_choice == "q":
        print("\nGame Over 👋")
        print(f"Final Score → You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("✅ You win this round!")
        user_score += 1

    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")
