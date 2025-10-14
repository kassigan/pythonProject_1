import requests
import pprint

# get Data

params  = {
    'q': 'html'
}

response = requests.get( url= 'https://api.github.com/search/repositories', params=params)
response_json = response.json()

print(response.status_code)  # Вывод статус-кода
print(response.headers)  # Вывод заголовка
print(response.text)  # Вывод основного текста (тела)
print(f"Ответ - {response.json()}")

# Request

params1 = {
    'userId': 1
}
response = requests.get( url='https://jsonplaceholder.typicode.com/posts', params=params1)

print(response.status_code)
print(response.text)

# Send Data

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post( url='https://jsonplaceholder.typicode.com/posts', json=data )

print(response.status_code)
print(response.text)


