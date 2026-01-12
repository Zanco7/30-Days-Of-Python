import random

#30-day Python challenge
print("------30-day Python challenge 8/30------")
print("Dice Roller 🎲")

while True:

    user= input("Roll the dice? (y/n)").lower()

    if user == "y":
        dice = random.randint(1, 6)
        print(f"Result is: {dice}🎲")

    elif user =="n":
        print("see you soon!")
        break
    else:
        print("Please enter y or n")
        continue
