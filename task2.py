import json
import requests 

key = 'c7325fc7-f04d-4cf8-ad05-4248def845a5'
year = '2025'
month = 5
country = 'RU'
lang = 'ru'
base_url
call = f'https://holidayapi.com/v1/holidays?key={key}&country={country}&year={year}&month={month}&pretty'


response = requests.post(call)
result = json.dumps(json.loads(response.text), indent=2)

print(result)

