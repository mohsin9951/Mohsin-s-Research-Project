# Lab Assignment 7
# Chosen publicly available API: OpenWeatherMap (Current Weather Data)
# API key: used my OpenWeatherMap API key
# Location: Troy, MI (ZIP 48083, US)

import requests

# API endpoint and parameters
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "zip": "48083,US",
    "units": "imperial",   # Fahrenheit
    "appid": "used my OpenWeatherMap API key"
}

try:
    # Send request
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Parse response JSON
    data = response.json()
    city = data.get("name", "Unknown City")
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Display weather report
    print("API Request Successful!\n")
    print(f"Weather Report for {city}, MI (48083):")
    print(f"  Condition   : {weather}")
    print(f"  Temperature : {temperature}°F (Feels like {feels_like}°F)")
    print(f"  Humidity    : {humidity}%")
    print(f"  Wind Speed  : {wind_speed} mph")

except requests.exceptions.RequestException as e:
    print("API request failed:", e)

