import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
response = urllib.request.urlopen(url)
data = response.read()
print("data")
user = '{"name":"thienhi", "age" : 18}'
with open('test.zip', 'w') as fobj:
    fobj.write(user)  # Tạo đối tương trong file
