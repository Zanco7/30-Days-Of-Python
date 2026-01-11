import time
from datetime import  datetime

#30-day Python challenge
print("------30-day Python challenge 7/30------")
print("Alarm Clock")

user_time = ""

while True:
    user_input = input("Pleas Enter the alarm time (HH:MM): ")
    try:
        valid_time = datetime.strptime(user_input,"%H:%M" )
        user_time = user_input
        break
    except ValueError:
        print("Invalid time! Please use the HH:MM format (e.g., 14:30).")
        continue
print(f"Alarm set for {user_time}. Waiting...")

while True:
    current_time = datetime.now().strftime("%H:%M")

    if user_time == current_time:
        print("⏰ALARM! Time reached!")
        break
    else:
        time.sleep(1)




