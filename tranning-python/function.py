def nhan(a, b):
    return a * b

x = nhan(5,2)

def hello():
    print('Hello ThienHi ',x)
hello()

def func(*f):
    print('Hello ' + f[4])
func('Thien','1','2','3')