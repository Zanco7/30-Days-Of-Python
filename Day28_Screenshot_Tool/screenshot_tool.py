# 30-day Python challenge
print("------30-day Python challenge 28/30------")
print("Screenshot Tool")

from PIL import ImageGrab
import time

def take_screenshot():
    print("📸 Screenshot will be taken in 3 seconds...")
    time.sleep(3)

    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

    print("✅ Screenshot saved as screenshot.png")

take_screenshot()
