class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def bark(self):
        print("%s이(가) 멍멍 짖습니다!" %(self.name))

dog=Dog("해피")
dog.bark()

class Shape:
    def __init__(self, color):
        self.color=color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

rect=Rectangle("Red", 10, 5)
print("색상: ", rect.color)
print("면적: ", rect.area())