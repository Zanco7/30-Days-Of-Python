# 30-day Python challenge
print("------30-day Python challenge 10/30------")
print("Contact Book 📒")

contacts = {}

while True:
    try:
        choice = int(input(
            "\n1. Add Contact"
            "\n2. View Contacts"
            "\n3. Search Contact"
            "\n4. Delete Contact"
            "\n5. Update Contact"
            "\n6. Exit"
            "\nChoose an option: "
        ))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # 1. Add Contact
    if choice == 1:
        name = input("Enter contact name: ").strip().lower()

        if name in contacts:
            print("Contact already exists.")
            continue

        try:
            phone = int(input("Enter phone number: "))
        except ValueError:
            print("Phone number must be numeric.")
            continue

        contacts[name] = phone
        print(f"{name.capitalize()} added successfully.")

    # 2. View Contacts
    elif choice == 2:
        if not contacts:
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(f"{name.capitalize()}: {phone}")

    # 3. Search Contact
    elif choice == 3:
        search = input("Enter contact name to search: ").strip().lower()
        if search in contacts:
            print(f"{search.capitalize()}: {contacts[search]}")
        else:
            print("Contact not found.")

    # 4. Delete Contact
    elif choice == 4:
        delete = input("Enter contact name to delete: ").strip().lower()
        if delete in contacts:
            contacts.pop(delete)
            print(f"{delete.capitalize()} deleted successfully.")
        else:
            print("Contact not found.")

    # 5. Update Contact
    elif choice == 5:
        name = input("Enter contact name to update: ").strip().lower()

        if name not in contacts:
            print("Contact not found.")
            continue

        try:
            new_phone = int(input("Enter new phone number: "))
        except ValueError:
            print("Phone number must be numeric.")
            continue

        contacts[name] = new_phone
        print(f"{name.capitalize()}'s phone number updated successfully.")

    # 6. Exit
    elif choice == 6:
        print("Goodbye! 👋")
        break

    else:
        print("Please choose a valid option (1–6).")
