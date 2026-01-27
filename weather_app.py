import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

def get_weather(city, api_key):
    # The URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)

        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"The weather in {city} is {temp}°C with {description}.")
        else:
            print(f"City not found. Error code: {data['cod']}")

    except Exception as e:
        print(f"An error occurred: {e}")


user_city = input("Enter city name: ")

get_weather(user_city, api_key)