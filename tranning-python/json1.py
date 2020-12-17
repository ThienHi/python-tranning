import json
import requests

response = requests.get('https://api.github.com/users/voduytuan/repos')

# data = json.load(response)
# data = response.read()

# print(data)
