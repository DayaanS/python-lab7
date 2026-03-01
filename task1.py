import json
import requests

city_name = 'Yakutsk'
key = 'a94852f4cdd3cd587f51b052b74e9847'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric&lang=ru')
result = json.loads(response.text)

city_name_ru = result['name']
desc = result['weather'][0]['description']
temp = result['main']['temp']
feels_like = result['main']['feels_like']
humidity = result['main']['humidity']
pressure = result['main']['pressure']


print(f'Погода в городе {city_name_ru} сейчас:')
print(desc)
print(f'Температура: {temp}; ощущается как {feels_like}')
print(f'Влажность: {humidity}')
print(f'Давление: {pressure}')
