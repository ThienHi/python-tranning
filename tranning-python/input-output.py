ten = raw_input('nhap ten: ')
msv = raw_input('Nhap msv: ')

txt = '35345435'
number = txt.isnumeric()
print(number)
# if number == true:
#     print('So')
# else: print('ko phai So')

print('Ten: ',ten)
print('MSV: ',msv)
print("kdl:",type(ten),type(msv))
print('Length Name : ', len(ten))
print(ten[1], ten[2])
print (ten[-3:-1])

# format text
ho = 'Nguyen Kim {}'
print(ho.format(ten))

name =  ho.replace('Kim','ThienHi')
print (name)