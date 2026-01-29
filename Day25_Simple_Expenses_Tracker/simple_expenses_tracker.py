#30-day Python challenge
print("------30-day Python challenge 25/30------")
print("Simple Expenses Tracker")

def initialize_expenses():
    return []

def add_expenses(expenses_storage):
    while True:
        try:
            expense_amount = float(input("Enter The Expense Amount (Must be a number): "))
        except ValueError:
            print("❌ Please enter a valid Amount.")
            continue

        if expense_amount <= 0:
            print("Expense Amount Must be greater than 0.")
            continue

        # category

        category = input("Enter The category: ").strip().lower()

        if not category:
            print("❌ Category Can't be an Empty.")
            continue

        # description

        description = input("Enter The Description: ").strip().lower()

        if not description:
            print("❌ Description Can't be an Empty.")
            continue

        expenses_storage.append((expense_amount, category, description))

        break



def view_expenses(expenses_storage):
    if not expenses_storage:
        print("No expenses recorded")

    else:
        for index, (expense_amount, category, description) in enumerate(expenses_storage, start=1):
            print(f"{index}. Amount: ${expense_amount} | Category: {category} | Description: {description}")



def total_expenses(expenses_storage):
    if not expenses_storage:
        print("No expenses recorded")

    else:
        total_amount = 0
        for expense_amount, category, description in expenses_storage:
            total_amount += expense_amount

        print(f"The total of all expenses is: ${total_amount:.2f}")


expenses_storage = initialize_expenses()


while True:
    try:
        user_choice= int(input("\nTrack Your expenses:"
        "\n1. Add expenses"
        "\n2. View expenses"
        "\n3. Show Total Expenses"
        "\n4. Exit the app\n"))
    except ValueError:
        print("Please Enter Valid Number")
        continue

    if user_choice == 1:
        add_expenses(expenses_storage)

    elif user_choice ==2:
        view_expenses(expenses_storage)

    elif user_choice ==3:
        total_expenses(expenses_storage)

    elif user_choice ==4:
        print("Good Bye")
        break

    else:
        print("❌ Choose between 1 and 4.")




