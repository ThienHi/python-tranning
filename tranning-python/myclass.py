class Users:
    def __init__(self, username,password, roles):
        self.username = username
        self.password = password
        self.roles = roles

    def myFunc(self):
        print ('Username: ' + self.username + '\nPassword: ' + self.password + '\nRole: ' + self.roles)


a = Users('ThienHi',str(12345),'Admin')
a.myFunc()

username = a.username
print username

class Person(Users):
    def __init__(self, username,password, roles,tk):
        Users.__init__(self,username,password,roles)
        self.tk = tk
    # def __init__(self,username,password, roles,tk):
    #     self.username = username
    #     self.password = password
    #     self.roles = roles
    def myFunction(self):
        print('Person '+self.username + '\nPassword '+ self.password + '\nRole '+self.roles + '\nTK '+self.tk)

b = Person('Hi',str(12345),'Not Admin','23423234')
b.myFunc()
b.myFunction()