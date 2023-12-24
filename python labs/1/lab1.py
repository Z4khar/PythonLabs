
class Webshop:
    count = 0
    id = 0
    name = ''
    age = ''
    gender = ''
    login = ''
    password = ''
    
    def __init__(self,name = 'Zakhar',age = 18, gender = 'Gigachad',login = '123',password = '123'):
        Webshop.count += 1
        self.id = Webshop.count
        self.age = age
        self.gender = gender
        self.login = login
        self.name = name
        self.password = password
    
    @property
    def id(self):
        return self.__id
    
    @property
    def age(self):
        return self.__age
            
    @property
    def password(self):
        return self.__password
        
    @age.setter
    def age(self,age_new):
        if age_new < 18:
            print('get out of here')
            self.__age = 18
            
        else:
            self.__age = age_new
    
    
    @id.setter
    def id(self,id):
        self.__id = id
        
    @password.setter
    def password(self,password):
        self.__password = password
        
    @staticmethod
    def print_all_information(_user_):
        print("Name: " + _user_.name)
        print("ID: " + str(_user_.id))
        print("Age: " + str(_user_.age))
        print("Gender: " + _user_.gender)
        print("Login: " + _user_.login)
        print("Password: " + _user_.password)
 
user1 = Webshop(age= 17)
user2 = Webshop()
print(Webshop.print_all_information(user1))

