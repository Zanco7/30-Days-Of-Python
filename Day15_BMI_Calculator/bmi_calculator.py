# 30-day Python challenge
print("------30-day Python challenge 15/30------")
print("BMI Calculator")

running = True

while running:
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
    except ValueError:
        print("❌ Please enter numbers only.")
        continue

    if weight <= 0:
        print("❌ Weight must be greater than zero.")
        continue

    if height <= 0:
        print("❌ Height must be greater than zero.")
        continue

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    while True:
        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()

        if again == "y":
            break
        elif again == "n":
            print("Goodbye! 👋")
            running = False
            break
        else:
            print("Please enter y or n.")
