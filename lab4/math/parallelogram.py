def parallelogram_area(length, height):
    area = length * height
    return area

length = float(input("Length: "))
height = float(input("Heigth: "))

area = parallelogram_area(length, height)
print("Area of a parallelogram:", area)