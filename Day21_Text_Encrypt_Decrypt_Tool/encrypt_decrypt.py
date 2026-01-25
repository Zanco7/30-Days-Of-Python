# 30-day Python challenge
print("------30-day Python challenge 21/30------")
print("Text Encrypt / Decrypt Tool 🔐")


def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char

    return result


running = True

while running:
    try:
        choice = int(input(
            "\nChoose an option:\n"
            "1. Encrypt Text\n"
            "2. Decrypt Text\n"
            "3. Exit\n"
            "👉 "
        ))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if choice == 1:
        text = input("Enter text to encrypt: ").strip()
        if not text:
            print("❌ Text cannot be empty.")
            continue

        try:
            key = int(input("Enter key (number): "))
        except ValueError:
            print("❌ Key must be a number.")
            continue

        encrypted_text = encrypt(text, key)
        print(f"🔐 Encrypted Text: {encrypted_text}")

    elif choice == 2:
        text = input("Enter text to decrypt: ").strip()
        if not text:
            print("❌ Text cannot be empty.")
            continue

        try:
            key = int(input("Enter key (number): "))
        except ValueError:
            print("❌ Key must be a number.")
            continue

        decrypted_text = decrypt(text, key)
        print(f"🔓 Decrypted Text: {decrypted_text}")

    elif choice == 3:
        print("Goodbye 👋")
        running = False

    else:
        print("❌ Choose between 1 and 3.")
