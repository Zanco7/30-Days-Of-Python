# 30-day Python challenge
print("------30-day Python challenge 26/30------")
print("Weather App (API Based)")

import requests


def get_weather(city_name):
    API_KEY = "YOUR_API_KEY_HERE"  # replace with your real API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("❌ City not found. Please try again.")
            return

        city = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print("\n🌍 Weather Information")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException:
        print("❌ Network error. Please check your internet connection.")


def main():
    while True:
        city_name = input("\nEnter city name: ").strip()

        if not city_name:
            print("❌ City name cannot be empty.")
            continue

        get_weather(city_name)

        choice = input("\nCheck another city? (y/n): ").strip().lower()
        if choice != "y":
            print("👋 Goodbye! Stay safe.")
            break


main()
