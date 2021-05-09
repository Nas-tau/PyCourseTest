# 5. Напишите код с использованием наследования.
class A(object):
    def __init__(self, name):
        print("Her name is " + name)

class B(A):
    def __init__(self):
        print("She's here")
        super().__init__("Erica")
C = B()


# 6. Напишите код с использованием инкапсуляции. 
class Car:
    maker = "BMW"
    def __init__(self, model):
        self.model = model
    
    @property
    def model(self):
        return self.model

    def getCarModel(self):
        return "Car model is " + self.model

car1 = Car("X6")
print(car1.getCarModel())

# 7. Напишите код с использованием полиморфизма. 
class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age >= 18:
            print("Pass")
        else:
            print("Accept")

    def display_info(self):
        print("Name: ", self.__name, "\tAge:", self.__age)

class Status(Adam):
    def __init__(self, name, age, marital_status):
        Adam.__init__(self, name, age)
        self.marital_status = marital_status

        def display_info(self):
            Adam.display_info(self)
            print("Marital status: ", self.marital_status)

person1 = Adam("Adam", 18)
person2 = Status("Abe", 44, "Single")
print(person1.display_info())
print(person2.display_info())

# 8. Дайте определение термину "абстракция". Опрелеления (txt формат) и код  (.py) залейте на гит хаб, 
# прикркпите ссылку (можете прикрепить общую ссылку со всеми заданиями)
from abc import ABC, abstractmethod
class Snake(ABC):
    @abstractmethod
    def hunt(self):
        print("Snake is hunting")

class Rattlesnake(Snake):
    def hunt(self):
        super().hunt()
        print("Rattlesnake is hunting")

animal = Rattlesnake()
animal.hunt()

# 10. "итератор"? 
a = [2,3,4,5]
f = [i**i for i in a]
print(f)
