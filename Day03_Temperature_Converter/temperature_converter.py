#30-day Python challenge
print("------30-day Python challenge 3/30------")

def celsius_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5/9

print("Temperature Converter 🌡️")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

whole_loop= True
while whole_loop:

    try:
        option = int(input("Please enter 1 or 2: "))
    except ValueError:
        print("Error: please enter numbers only.\n")
        continue

    if option not in (1, 2):
        print("Try Again: choose Only 1 or 2 please.\n")
        continue
    converter_loop = True
    while converter_loop:
        try:
            converter = float(input("Enter the temperature value please: "))
        except ValueError:
            print("Error: please enter numbers only.\n")
            continue

        if option == 1:
            print(f"Result: {celsius_fahrenheit(converter):.2f} °F")

        elif option == 2:
            print(f"Result: {fahrenheit_celsius(converter):.2f} °C")

        again_loop= True
        while again_loop:

            again = input("Convert another temperature? (y/n): ").lower()
            if again == "y":
                again_loop = False
                converter_loop = False
            elif again == "n":
                print("Goodbye! 👋")
                again_loop = False
                converter_loop = False
                whole_loop = False
            else:
                print("Please enter y or n.")












