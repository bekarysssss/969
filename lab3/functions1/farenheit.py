def fahrenheit_to_celsius(fr):
    cl = (5/9) * (fr - 32)
    return cl

fr = 100
result = fahrenheit_to_celsius(fr)
print(f"{result}")