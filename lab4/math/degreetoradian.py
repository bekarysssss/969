def degree_to_radian(degree):
    radian = degree * 3.14/180
    return radian

degree = float(input("Degree: "))


radian = degree_to_radian(degree)
print("Radian value:", radian)
