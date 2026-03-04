import json
import requests 
import os

URL = 'https://holidayapi.com/v1/holidays'
key = os.getenv('KEY2')
params = {
    'key': key,
    'country': 'RU',
    'year': '2025',
    'lang': 'ru',
    'pretty': True,
}
limit = 5

response = requests.post(URL, params=params)
data = json.loads(response.text)
holidays = data['holidays']

for i in range(len(holidays)):
    if i > limit:
        break
    name = holidays[i]['name']
    date = holidays[i]['date']
    weekday = holidays[i]['weekday']['date']['name']
    print(f'{name}: {date}, {weekday}')    


