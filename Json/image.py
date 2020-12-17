import requests

url = requests.get(
    'https://media.gettyimages.com/photos/giant-panda-bear-picture-id475636556?s=170667a')

print(url.status_code)

with open('panda.png', 'wb') as png:
    png.write(url.content)
