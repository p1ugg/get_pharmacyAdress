from pprint import pprint

import requests

KEY = '40d1649f-0493-4b70-98ba-98533de7710b'
a = input('Введи в город и адрес(место), где ты хочешь найти аптеку:\n')
url = f'https://geocode-maps.yandex.ru/1.x'

parameters = {
    'geocode': a,
    'lang': 'ru_RU',
    'kind': 'district',
    'apikey': KEY,
    "format": "json"
}
req = url + '?' + '&'.join(['='.join(i) for i in parameters.items()])
res = requests.get(req).json()
print(res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][3]['name'])
