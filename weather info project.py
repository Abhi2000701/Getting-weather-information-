import requests
from pprint import pprint

API_key= 'd81286d4ebc5e01b23064167d6108adb'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data  = requests.get(base_url).json()

pprint(weather_data)