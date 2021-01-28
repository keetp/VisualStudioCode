# lecture from Jan 26th 2021

class Point:
    """representation of a point in 2D cartesian plane

    attributes: x and y co-ordinates
    """

    # initializing the object with the x and y coord values
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # formatting how the object is printed
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


# example of overriding a class with an inherited class.
class LabeledPoint(Point):

    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

    def __str__(self):
        return super().__str__() + f", ({self.label})"


point = Point(4, 5)
l_point = LabeledPoint(7, 6, 'here')
print(l_point)