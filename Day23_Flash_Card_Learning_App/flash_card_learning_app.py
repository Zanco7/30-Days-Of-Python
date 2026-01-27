import random

# 30-day Python challenge
print("------30-day Python challenge 23/30------")
print("Flash Card Learning App")

def initialize_flashcards():
    return {}

def add_flashcard(flash_cards):
    question = input("Enter the Question: ").strip().lower()
    answer = input("Enter the Answer: ").strip().lower()

    if not question or not answer:
        print("❌ Question or Answer cannot be empty.")
        return

    flash_cards[question] = answer
    print("✅ Flashcard added successfully!")

def study_flashcards(flash_cards):
    if not flash_cards:
        print("❌ No flashcards available.")
        return

    for index, (question, answer) in enumerate(flash_cards.items(), start=1):
        print(f"\nQuestion {index}: {question}")
        print(f"Answer {index}: {answer}")

def quiz_flashcards(flash_cards, score):
    if not flash_cards:
        print("❌ No flashcards available.")
        return score

    while True:
        question = random.choice(list(flash_cards.keys()))
        correct_answer = flash_cards[question]

        print(f"\nQuestion: {question}")
        user_answer = input("Your answer (or q to quit): ").strip().lower()

        if user_answer == "q":
            print("👋 Exiting quiz...")
            break

        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {correct_answer}")

        print(f"Current Score: {score}")

    return score

def view_flashcards(flash_cards):
    if not flash_cards:
        print("❌ No flashcards available.")
        return

    for index, question in enumerate(flash_cards.keys(), start=1):
        print(f"{index}. {question}")


flash_cards = initialize_flashcards()
score = 0

while True:
    try:
        choice = int(input(
            "\nChoose an option:"
            "\n1. Add Flashcard"
            "\n2. Study Mode"
            "\n3. Quiz Mode"
            "\n4. View Flashcards"
            "\n5. Exit\n"
        ))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if choice == 1:
        add_flashcard(flash_cards)

    elif choice == 2:
        study_flashcards(flash_cards)

    elif choice == 3:
        score = quiz_flashcards(flash_cards, score)

    elif choice == 4:
        view_flashcards(flash_cards)

    elif choice == 5:
        print(f"👋 Goodbye! Final Score: {score}")
        break

    else:
        print("❌ Choose between 1 and 5.")
