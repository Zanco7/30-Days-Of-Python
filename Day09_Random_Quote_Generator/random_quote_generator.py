import random

#30-day Python challenge
print("------30-day Python challenge 9/30------")
print("Today's Quote")

quotes = ["Start where you are. Use what you have. Do what you can.",
          "Small steps every day lead to big results.",
          "Don’t watch the clock; do what it does. Keep going.",
          "Learning to code is learning how to think.",
          "Consistency beats motivation.",
          "Your future is created by what you do today.",
          "Mistakes are proof that you are trying.",
          "Code a little. Learn a lot.",
          "Progress, not perfection.",
          "Every expert was once a beginner."]

running = True


while running:

    print(random.choice(quotes))

    while True:
        again= input("Do you want another quote? (y/n) ").lower()
        if again == "y":
            break
        elif again == "n":
            print("Goodbye! 👋")
            running = False
            break
        else:
            print("Please enter y or n")
            continue
