import math

class MyShape:
    pass

class Rectangle(MyShape):
    def __init__(self, x_top_left, y_top_left, length, width):
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

class Circle(MyShape):
    def __init__(self, x_center, y_center, radius):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2
print("for rectangle: ")
Rx = int(input("x coordinate: "))
Ry = int(input("y coordinate: "))
length = int(input("length: "))
width = int(input("width: "))
rectangle = Rectangle(Rx, Ry, length, width)
print("Area of rectangle: ", rectangle.getArea())

print("for cirle: ")
Cx = int(input("x cordinate: "))
Cy = int(input("y cordinate: "))
Cradius = int(input("radius: "))
circle = Circle(Cx, Cy, Cradius)
print("Area of circle: ", circle.getArea())
