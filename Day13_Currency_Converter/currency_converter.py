#30-day Python challenge
print("------30-day Python challenge 13/30------")

print("Currency Converter")

currencies= {"USD" : 1.0,
"EUR" : 0.92,
"GBP" : 0.78,
"SOS" : 570.0,
"KES" : 160.0
}

print("Available Currencies:", ", ".join(currencies.keys()))

running = True

while running:
    try:
        amount = float(input("Enter Your Amount: "))
    except ValueError:
        print("Please enter a valid Amount.")
        continue

    if amount <= 0:
        print("Amount must be greater than zero")
        continue

    from_currency_rate = input("Enter From Currency (USD, EUR, GBP, KES and SOS): ").strip().upper()

    to_currency_rate = input("Enter To Currency (USD, EUR, GBP, KES and SOS): ").strip().upper()

    if from_currency_rate not in currencies or to_currency_rate not in currencies:
        print("Please choose valid currencies")
        continue

    else:
        converted_amount = (amount / currencies[from_currency_rate]) * currencies[to_currency_rate]
        print(f"Your Currency is: {converted_amount:.2f} {to_currency_rate}")

    while True:

        choice = input("Convert Again? (y/n)").lower()

        if choice == "y":
            break

        elif choice == "n":
            print("Goodbye 👋")
            running = False
            break
        else:
            print("Please choose y or n")
            continue
