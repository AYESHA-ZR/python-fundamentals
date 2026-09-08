# api project
# weather app
import requests
city = input("enter city name = ")
url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name":city,
    "count":1,
    "language":"en",
    "format":"json"
}

try:
    response = requests.get(url,params=params,timeout=10)
    response.raise_for_status()
    
    data = response.json()
   
    
    if "results" in data and data["results"]:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        
            
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code"
        }
            
        weather_response = requests.get(weather_url,params=weather_params,timeout=10)
            
        weather_response.raise_for_status()
            
        weather_data = weather_response.json()
        
        temperature = weather_data["current"]["temperature_2m"]
        wind_speed = weather_data["current"]["wind_speed_10m"]
        weather_code = weather_data["current"]["weather_code"]
        
        weather_conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
            }
        condition = weather_conditions.get(weather_code,"unknown weather")
        
        print()
        print("----- WEATHER INFO -----")
        print("CITY        =", city)
        print("TEMPERATURE =", temperature, "°C")
        print("WIND SPEED  =", wind_speed, "km/h")
        print("CONDITION   =", condition)
    else:
        print("city not found.")
    
except requests.exceptions.RequestException:
    print("---API request failed---")
    
    
    