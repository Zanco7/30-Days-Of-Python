# Day 26 — Weather App (API Based)

This project is a command-line **Weather App** built using Python and a real external API as part of my **30-Day Python Challenge**.

The app fetches live weather data for any city using the **OpenWeatherMap API**.

## Features
- Get real-time weather data by city name
- Displays:
  - Temperature (°C)
  - Weather condition
  - Humidity
  - Wind speed
- Handles invalid city names
- Handles network errors
- Uses API requests with parameters

## How It Works
1. The user enters a city name.
2. The app sends a request to the OpenWeatherMap API.
3. Weather data is fetched and parsed from JSON.
4. The results are displayed in a clean format.
5. The user can check multiple cities in one session.

## Requirements
- Python 3
- `requests` library
- OpenWeatherMap API key

Install requests if not installed:
```bash
pip install requests
