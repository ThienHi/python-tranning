import requests
import json

payload = {'page': 2, 'count': 26}
data = {'username': 'ThienHi', 'age': 20}

get = requests.get('http://httpbin.org/get', params=payload)

url = requests.post('https://httpbin.org/post', json=data)

basicAuth = requests.get(
    'http://httpbin.org/basic-auth/thienhi/kimthien2603', auth=('thienhi', 'kimthien2603'))

data = url.json()

# print(data['json'])

# print(url.status_code)
# print(url.text)
# print(url.url)
print(basicAuth.status_code)
