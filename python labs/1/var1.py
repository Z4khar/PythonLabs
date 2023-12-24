class Car:
    #count = 0
    model = ''
    power = 0
    age = 0
    color = ''
    
    def __init__(self,model = "Lada",power = 95, age = 3, color = "Gray"):
        #Car.count += 1
        self.model = model
        self.power = power
        self.age = age
        self.color = color
    
    @property
    def model(self):
        return self.__model
        
    @model.setter
    def model(self,model):
        self.__model = model
        
    @staticmethod
    def print_all_information(_uss_):
        print("model: " + _uss_.model)
        print("Power: " + str(_uss_.power))
        print("Age: " + str(_uss_.age))
        print("Color: " + _uss_.color)
 
uss = Car()
print(Car.print_all_information(uss))

