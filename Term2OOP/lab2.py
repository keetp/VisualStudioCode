""" Lab 2: Object Oriented Programming. Creating a Point and a Rectangle class."""


# point class with attributes x-coord and y-coord
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


# rectangle class with attributes Point(x,y), height and width

class Rectangle:
    def __init__(self, corner_coord, height, width):
        self.corner_coord = corner_coord
        self.height = height
        self.width = width

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return f"Corner Point: {self.corner_coord}, Height = {self.height}, Width = {self.width}"

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def transpose(self):
        h = self.height
        w = self.width
        self.height = w
        self.width = h


r = Rectangle(Point(0, 0), 10, 5)
p = r.perimeter()
a = r.area()
r.transpose()
print(r)
