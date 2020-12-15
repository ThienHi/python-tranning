dictionary = {
    "person": [{
        "name": "ThienHi",
        "age": 25
    },
        {
        "name": "ThienHi",
        "age": 25
    },
        {
        "name": "Kim",
        "age": 22
    }
    ]
}
x = dictionary.get("person")
y = dictionary.keys()
z = dictionary.values()
# update = dictionary.update({'age': 20})

# print(dictionary['name'])
print('X: ', x)
# print('Key : ', y, 'Value: ', z)

dictionary['name'] = 'Peter'
print(dictionary)

for i, e in dictionary.items():
    print(e, i)
