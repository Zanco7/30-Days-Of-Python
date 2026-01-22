# 30-day Python challenge
print("------30-day Python challenge 18/30------")
print("Simple Login System")


def users_accounts():
    """Initialize and return empty user storage"""
    return {}


def register(users):
    name = input("Enter username: ").strip().lower()

    if not name:
        print("❌ Username cannot be empty.")
        return

    if name in users:
        print("❌ Username already exists.")
        return

    password = input("Enter password: ").strip()

    if not password:
        print("❌ Password cannot be empty.")
        return

    users[name] = password
    print("✅ Registration successful!")


def login(users):
    name = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()

    if not name or not password:
        print("❌ Username and password cannot be empty.")
        return

    if name not in users:
        print("❌ Username not found.")
        return

    if users[name] == password:
        print(f"✅ Welcome back, {name}!")
    else:
        print("❌ Incorrect password.")



users = users_accounts()


while True:
    try:
        choice = int(input(
            "\n1. Register"
            "\n2. Login"
            "\n3. Exit"
            "\nChoose an option: "
        ))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if choice == 1:
        register(users)

    elif choice == 2:
        login(users)

    elif choice == 3:
        print("👋 Goodbye!")
        break

    else:
        print("❌ Please choose a valid option (1–3).")
