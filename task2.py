'''
Возьмите сайт из вашего варианта. 
Разберитесь, как работает его API, 
какие данные при помощи него можно получить. 
Сформируйте запрос с параметрами и получите ответ в 
формате ```.json```. Возможно, потребуется библиотека ```json```.
Сделайте структурированный вывод информации 
(5-7 полей, форматирование на усмотрение студента).
'''

import json
import requests 

key = 'c7325fc7-f04d-4cf8-ad05-4248def845a5'
year = '2025'
month = 5
country = 'RU'
lang = 'ru'
call = f'https://holidayapi.com/v1/holidays?key={key}&country={country}&year={year}&month={month}&pretty'


response = requests.post(call)
result = json.dumps(json.loads(response.text), indent=2)

print(result)

