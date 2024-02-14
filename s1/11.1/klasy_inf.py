class ParrentClass:
    def speak(self):
        print("JESTEM rodzicem")
        
class ChildClass(ParrentClass):
    def speak(self):
        super().speak()#dziedziczona funkcja
        print("jstem dzieckiem")
        
child=ChildClass()
child.speak()
parrent=ParrentClass()
parrent.speak()


            #polimorfizm - dziala podobnie
def area(shape):
    return shape.calculate_area()

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height
    
    
circle=Circle(4)
rectangle=Rectangle(3,4)
print(f"pole kola= {area(circle)}")
print(f"pole prostokata= {area(rectangle)}")

        #inne rozw.
class Animal:
    def speak(self):
        pass
class Dog:
    def speak(self):
        return "Hau!"
class Cat:
    def speak(self):
        return "Miau!"
def make_animal_speak(animal):
    return animal.speak()

dog=Dog()
cat=Cat()
print(make_animal_speak(dog))
print(make_animal_speak(cat))




        #klasy abstrakcyjne
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(shape):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height


circle=Circle(4)
rectangle=Rectangle(3,4)
print(f"pole kola= {circle.calculate_area()}")
print(f"pole prostokata= {rectangle.calculate_area()}")




            #magiczne metody
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age} lat"
person=Person("Alicja",33)
print(str(person))