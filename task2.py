import json
import requests 

url = 'https://holidayapi.com/v1/holidays'
key = 'c7325fc7-f04d-4cf8-ad05-4248def845a5'
params = {
    'key': 'c7325fc7-f04d-4cf8-ad05-4248def845a5',
    'country': 'RU',
    'year': '2025',
    'month': 2,
    'lang': 'ru',
    'pretty': True,
}

response = requests.post(url, params=params)
result = json.dumps(json.loads(response.text), indent=2)

print(result)

