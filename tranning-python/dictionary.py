dictionary = {'name' : 'thienHi', 'age' : 18, 'gender': 'male'}
x =dictionary.get('name')
y = dictionary.keys()
z = dictionary.values()
update = dictionary.update({'age':20})

print dictionary['name']
print 'X: ',x
print 'Key : ',y,'Value: ',z

dictionary['name']= 'Peter'
print dictionary

for i,e in dictionary.items() :
    print e , i