import json
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
key = 'a94852f4cdd3cd587f51b052b74e9847'
city_name = 'Yakutsk'
params = {
    'appid': key,
    'q': city_name,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.post(url, params=params)
result = json.loads(response.text)

city_name_ru = result['name']
desc = result['weather'][0]['description']
temp = result['main']['temp']
feels_like = result['main']['feels_like']
humidity = result['main']['humidity']
pressure = result['main']['pressure']

print(f'Погода в городе {city_name_ru} сейчас: {desc}')
print(f'Температура: {temp}; ощущается как {feels_like}')
print(f'Влажность: {humidity}')
print(f'Давление: {pressure}')
