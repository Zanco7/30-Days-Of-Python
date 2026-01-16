import time

print("------30-day Python challenge 12/30------")
print("Basic Stopwatch")

while True:
    print("\n1. Start Stopwatch")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        input("Press Enter to START")
        start_time = time.time()

        input("Press Enter to STOP")
        end_time = time.time()

        elapsed_time = end_time - start_time

        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60

        print(f"Elapsed Time: {minutes} min {seconds:.2f} sec")

    elif choice == "2":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.")
