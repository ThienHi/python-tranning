import json

c = '''{"name": "Mark",
       "age": 30,
       "city": "New York"
       }'''

b = json.loads(c)

print(b["name"])

x = '{ "name":"John", "age":25, "city":"New York"}'

y = json.loads(x)

print(y)
print(y["age"])

print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76, indent=6))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
