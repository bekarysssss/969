class Shape:

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle_instance = Rectangle(9, 6)
print("Area of rectangle:", rectangle_instance.area())
