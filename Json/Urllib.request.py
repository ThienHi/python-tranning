import urllib.request
import json
url = urllib.request.urlopen('https://api.github.com/users/voduytuan/repos')

# print(url)

print(url.geturl())

data = json.load(url)

print(data)

url.info()

headers = url.info()

# print(headers.as_string())

# print(url.getcode())
