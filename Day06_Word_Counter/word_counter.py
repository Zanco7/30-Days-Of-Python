#30-day Python challenge
print("------30-day Python challenge 6/30------")

print("Word Counter")

while True:

    user_words = input("Enter your text:\n").strip()

    characters_count = "".join(user_words.split())
    print(f"characters count is: {len(characters_count)}")

    words_count = user_words.split()
    print(f"words count is: {len(words_count)}")

    sentences_count = sum(user_words.count(x) for x in ".!?")
    print(f"Sentences count: {sentences_count}")

    while True:
        again = input("Count another text? (y/n): ").lower()
        if again == "y":
            break
        elif again == "n":
            print("Goodbye! 👋")
            exit()
        else:
            print("Please enter 'y' or 'n'.")


