import json
import requests
import os

URL = 'https://api.openweathermap.org/data/2.5/weather'
key = os.getenv('KEY1')
city_name = 'Yakutsk'
params = {
    'appid': key,
    'q': city_name,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.post(URL, params=params)
data = json.loads(response.text)

city_name_ru = data['name']
desc = data['weather'][0]['description']
temp = data['main']['temp']
feels_like = data['main']['feels_like']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print(f'Погода в городе {city_name_ru} сейчас: {desc}')
print(f'Температура: {temp}; ощущается как {feels_like}')
print(f'Влажность: {humidity}')
print(f'Давление: {pressure}')