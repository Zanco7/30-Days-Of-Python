# 30-day Python challenge
print("------30-day Python challenge 19/30------")
print("Multiplication Table Tool")

def multiblication_tool(number):
    """Print multiplication table from 1 to 10"""
    print(f"\nMultiplication Table for {number}")
    print("-" * 30)
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")



running= True

while running:
    try:
        num = int(input("Enter Valid Integer please: "))
    except ValueError:
        print("Error: please enter numbers only.\n")
        continue

    multiblication_tool(num)

    again = input("\nDo you want another table? (y/n): ").strip().lower()

    if again != "y":
        print("Goodbye! 👋")
        break



