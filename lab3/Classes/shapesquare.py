class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length

shape_instance = Shape()
print("Area shape:", shape_instance.area())

square_instance = Square(5)
print("Area square:", square_instance.area())
