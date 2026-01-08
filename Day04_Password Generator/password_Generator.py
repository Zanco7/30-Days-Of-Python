import random
import string

#30-day Python challenge
print("------30-day Python challenge 4/30------")
print("Password Generator")

while True:

    character_pool = ""

    try:
        pwd_len = int(input("Enter the password length: "))
    except ValueError:
        print("Error: please enter numbers only.\n")
        continue

    letters = input("include letters? (y/n): ").lower()
    numbers = input("include numbers? (y/n): ").lower()
    symbols = input("include symbols? (y/n): ").lower()

    if letters == "y":
        character_pool += string.ascii_lowercase + string.ascii_uppercase
    if numbers == "y":
        character_pool += string.digits
    if symbols == "y":
        character_pool += string.punctuation
    if character_pool == "":
        print("Please select at least one option")
        continue

    password = random.choices(character_pool,k= pwd_len)
    print("Your password is:", "".join(password))

    again = input("Generate another password? (y/n): ").lower()
    if again == "n":
        print("Goodbye! 👋")
        break
