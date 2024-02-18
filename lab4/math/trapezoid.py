def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Height:"))
base1 = float(input("Value of base1: "))
base2 = float(input("Value of base2: "))


area = trapezoid_area(base1, base2, height)
print("Area of a trapezoid:", area)