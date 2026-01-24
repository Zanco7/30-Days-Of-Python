import time

# 30-day Python challenge
print("------30-day Python challenge 20/30------")
print("Simple Reminder App")

def get_reminder():
    massege = input("Enter The Reminder Message: ").strip()

    if not massege:
        print("Reminder Massage Can't be an Empty")
        return None
    return massege

def get_time():
    try:
        seconds = int(input("Please enter the alarm time in seconds:  "))
        if seconds <= 0:
            print("Seconds Must be Greater Then Zero")
            return None
        return seconds
    except ValueError:
        print("Please enter a valid number.")
        return None


def set_reminder(massege, seconds):
    print(f"\n⏳ Reminder set for {seconds} seconds...")
    time.sleep(seconds)
    print(f"\n🔔 REMINDER: {massege}")


while True:
    reminder = get_reminder()
    if reminder is None:
        continue

    reminder_time = get_time()

    if reminder_time is None:
        continue

    set_reminder(reminder, reminder_time)

    again = input("Do you want to set another reminder? (y/n): ").strip().lower()
    if again != "y":
        print("👋 Goodbye!")
        break
