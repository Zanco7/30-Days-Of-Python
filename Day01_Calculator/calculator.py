#30-day Python challenge
# Day 1 — Python Calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("WELCOME TO OUR CALCULATOR")

previous_result = None

while True:

    if previous_result is not None:
        use_prev= input("Do you want to use the previous result as the first number? (y/n): ").lower()
        if use_prev =="y":
            num1= previous_result
            print(f"Previous result is: {num1}")
        else:
            try:
                num1 = float(input("Enter the First Number please: "))
            except ValueError:
                print("Error: please enter numbers only.\n")
                continue
    else:
        try:
            num1 = float(input("Enter the First Number please: "))
        except ValueError:
            print("Error: please enter numbers only.\n")
            continue

    try:
        num2 = float(input("Enter the Second Number please: "))
    except ValueError:
        print("Error: please enter numbers only.\n")
        continue
    operator = input("Choose the Operator (+, -, *, /): ")

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = sub(num1, num2)
    elif operator == "*":
        result = mul(num1, num2)
    elif operator == "/":
        try:
            result = div(num1, num2)
        except ZeroDivisionError:
            print("Error: you cannot divide by zero.\n")
            continue
    else:
        print("Something is wrong: unknown operator.\n")
        continue

    print(f"The Result is: {result}")
    previous_result = result

    again= input("Do you want to do another calculation? (y/n): ").lower()
    if again == "n":
        print("Goodbye! 👋")
        break


