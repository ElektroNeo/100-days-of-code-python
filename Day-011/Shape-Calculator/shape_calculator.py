import math

class Rectangle:
    # Init class function
    def __init__ (self, w, h):
        self.h = h
        self.w = w
    # Class string representation
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.w, self.h)
    # Set width of rectangle
    def set_width(self, w):
        self.w = w
    # Set height of rectangle
    def set_height(self, h):
        self.h = h
    # Get area of rectangle
    def get_area(self):
        return self.w*self.h
    # Get perimeter of rectangle
    def get_perimeter(self):
        return (2*self.w+2*self.h)
    # Get diagonal of rectangle
    def get_diagonal(self):
        return ((self.w**2 + self.h**2) ** .5)
    # Set picture of rectangle if it is small
    def get_picture(self):
        picture = str()
        if self.w > 50 or self.h > 50:
            return "Too big for picture."
        for h in range(self.h):
            for w in range(self.w):
                picture += '*'
            picture += '\n'
        return picture
    # Get amount of shape inside rectangle
    def get_amount_inside(self, shape):
        return math.floor(self.h/shape.h)*math.floor(self.w/shape.w)

class Square(Rectangle):
    # Init class function
    def __init__(self, side):
        self.side = side
        self.h = side
        self.w = side
    # String representation of square
    def __str__(self):
        return "Square(side={})".format(self.side)
    # Set side of square
    def set_side(self, side):
        self.side = side
        self.h = side
        self.w = side
    # Set width of square
    def set_width(self, w):
        self.side = w
        self.w = w
        self.h = w
    # Set height of square
    def set_height(self, h):
        self.side = h
        self.h = h
        self.w = h