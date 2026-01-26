#30-day Python challenge
print("------30-day Python challenge 22/30------")
print("Notes App")

def all_notes():
    return []

def add_notes(notes):
    new_note = input("Add New Note \n")
    if not new_note:
        print("Please Enter somthing")
        return

    notes.append(new_note)
    print(f"{new_note} Added Successfully")
    return

def view_notes(notes):
    if not notes:
        print("Your Note list is empty!")
        return
    else:
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")
        return

def delete_notes(notes):
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    if not notes:
        print("No notes to delete.")
        return
    try:
        delete_note = int(input("Enter the number of the note to delete:"))
    except ValueError:
        print("Choose Valid Number please.")
        return

    index = delete_note - 1
    if 0 <= index < len(notes):
        notes.pop(index)
        print("Task removed!")
    else:
        print("Error: Invalid task number.")
        return


notes = all_notes()

running = True

while running:
    try:
        user_choice = int(input("Select one Please:"
                                "\n1. Add Note"
                                "\n2. View Notes"
                                "\n3. Delete Notes"
                                "\n4. Exit\n"))
    except ValueError:
        print("Choose a Number pls")
        continue


    if user_choice == 1:
        add_notes(notes)

    elif user_choice == 2:
        view_notes(notes)

    elif user_choice == 3:
        delete_notes(notes)

    elif user_choice == 4:
        print("Goodbye! 👋")
        break




