#30-day Python challenge
print("------30-day Python challenge 5/30------")

print("To Do List App")

tasks = []

while True:
    try:
        user_choice= int(input("Select one Please:\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit\n"))
    except ValueError:
        print("Choose a Number pls")
        continue

    if user_choice == 1:
        new_task = input("Add New Task \n")
        tasks.append(new_task)
        print("Added Successfully!")

    elif user_choice == 2:
        if not tasks:
            print("Your task list is empty!")
        else:
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")

    elif user_choice == 3:
        if not tasks:
            print("Your task list is empty!")
        else:
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")
            try:
                remove_task = int(input("Enter the Number of Task You Need to Remove pls: "))
            except ValueError:
                print("Choose the right task number  pls")
                continue
            index = remove_task - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("Task removed!")
            else:
                print("Error: Invalid task number.")
    elif user_choice == 4:
        print("Goodbye! 👋")
        break


