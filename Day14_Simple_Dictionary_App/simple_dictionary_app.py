#30-day Python challenge
print("------30-day Python challenge 14/30------")

print("Simple Dictionary App")

def load_dictionary():
    """Initialize and return an empty dictionary"""
    return {}

def add_word(dictionary):
    word = input("Enter New Word: ").strip().lower()

    # empty input word check
    if not word:
        print("❌ Word cannot be empty.")
        return

    # duplicate word check
    if word in dictionary:
        print("This word already exists.")
        return

    meaning = input("Enter the meaning of the word: ").strip().lower()

    if not meaning:
        print("❌ Meaning cannot be empty.")
        return

    dictionary[word] = meaning
    print(f"{word.capitalize()} added successfully.")


def search_word(dictionary):
    search = input("Enter the word You need to search: ").strip().lower()
    if not search:
        print("❌ Search cannot be empty.")
        return

    if search in dictionary:
        print(f"{search.capitalize()}:{dictionary[search]}")
    else:
        print("NOT FOUND")

def view_all_words(dictionary):
    if not dictionary:
        print("No words Found")
        return

    for word, meaning in dictionary.items():
        print(f"{word.capitalize()}:{meaning.capitalize()}")


dictionary = load_dictionary()

running = True

while running:

    try:
        user_choice = int(input(
        "1. Add Word"
        "\n2. Search Word"
        "\n3. View All Words"
        "\n4. Exit"
        "\nChoose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue


    if user_choice == 1:
        add_word(dictionary)

    elif user_choice == 2:
        search_word(dictionary)

    elif user_choice == 3:
        view_all_words(dictionary)

    elif user_choice == 4:
        print("Goodbye! 👋")
        break
    else:
        print("Please choose a valid option (1–4).")
