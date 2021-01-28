""" Lab 2: Object Oriented Programming. Creating a Point and a Rectangle class."""


# QUESTION 1
class Dog:
    """ A basic representation of a dog.

    attributes: self, name, breed, age
    """

    # initializing dog object
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("ruff ruff")

    # formatting output to be human legible
    def __str__(self):
        return f"{self.name}, {self.breed}, {self.age}"

    # 3 get methods which return dog object's name, breed and age respectively
    def getName(self):
        return self.name

    def getBreed(self):
        return self.breed

    def getAge(self):
        return self.age


# helper function to check for deep equality in dog objects
def sameDog(dog1, dog2):
    dog1 = [dog1.getName(), dog1.getBreed(), dog1.getAge()]
    dog2 = [dog2.getName(), dog2.getBreed(), dog2.getAge()]
    return dog1 == dog2


# instantiating 2 dogs (james and franko)
james = Dog('James', 'Pitt Bull', 7)
franko2 = Dog('Franko', 'Pitt Bull', 7)
franko = Dog('Franko', 'Pitt Bull', 7)

# checking shallow equality
print(james is franko)
# using sameDog function to check deep equality
# example where deep equality is true
print(sameDog(franko2, franko))
# example where deep equality is false
print(sameDog(franko, james))

#######################################################################################################################
# QUESTION 2
class Point:
    """representation of a point in 2D cartesian plane

    attributes: x and y co-ordinates
    """

    # initializing the object with the x and y coord values
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # formatting how the object is printed
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


# rectangle class with attributes Point(x,y), height and width

class Rectangle:
    """Building a rectangle

    attributes: corner co-ordinate in 2D space, height, width
    """

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


# calling object methods and printing for testing purposes. remove comment symbols to print yourself.
r = Rectangle(Point(0, 0), 10, 5)
p = r.perimeter()
a = r.area()
r.transpose()
# print(r.__doc__)
