import requests
import json
userdata = '{"firstname": "John", "lastname": "Doe", "password": "1234"}'
resp = requests.get('https://api.github.com')

data = json.dumps(userdata)

print(data)

if resp.status_code == 200:
    print("Success")
else:
    print("Not found")
