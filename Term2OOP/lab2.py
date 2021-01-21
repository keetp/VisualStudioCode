""" Lab 2: Object Oriented Programming. Creating a Point and a Rectangle class."""


# point class with attributes x-coord and y-coord
class Point:    
    # initializing the object with the x and y coord values
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # formatting how the object is printed
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


# rectangle class with attributes Point(x,y), height and width

class Rectangle:    
    # initializing the rectangle object with attributes corner coord (x and y value), height and width
    def __init__(self, corner_coord, height, width):
        self.corner_coord = corner_coord
        self.height = height
        self.width = width  

    # returns the width
    def getWidth(self): 
        return self.width

    # returns the height
    def getHeight(self):
        return self.height

    # formatting how the object is printed
    def __str__(self):
        return f"Corner Point: {self.corner_coord}, Height = {self.height}, Width = {self.width}"

    # returns the area of the rectangle
    def area(self):
        return self.height * self.width

    # returns perimeter of the rectangle
    def perimeter(self):
        return 2 * self.height + 2 * self.width

    # reverses the width and height values
    def transpose(self):
        h = self.height
        w = self.width
        self.height = w
        self.width = h


# calling object methods and printing for testing purposes
r = Rectangle(Point(0, 0), 10, 5)
p = r.perimeter()
a = r.area()
r.transpose()
print(r)
