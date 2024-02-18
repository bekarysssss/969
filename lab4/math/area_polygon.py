import math

def area_regular_polygon(a, b):
    return (0.25 * a * b ** 2) / math.tan(math.pi / a)

a = int(input("Input number of sides: "))
b = float(input("Input the length of a side: "))

area = area_regular_polygon(a, b)
print("The area of the polygon is:", area)
