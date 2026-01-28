#30-day Python challenge
print("------30-day Python challenge 24/30------")
print("Prime Number Checker")

running = True

while running:

    try:
        user_number = int(input("Enter the Number: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if user_number <= 1:
        print(f"Number {user_number} is not Prime")
    else:
        is_prime = True

        for i in range(2, int(user_number ** 0.5) + 1):
            if user_number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"The Number {user_number} is Prime")

        else:
            print(f"Number {user_number} is not Prime")

    while True:
        again = input("Do you want to Check another Number? (y/n) ").lower()
        if again == "y":
            break
        elif again == "n":
            print("Goodbye! 👋")
            running = False
            break
        else:
            print("Please enter y or n")
            continue
