a = int(input("First number: "))
b = int(input("Second number: "))
def squares_generator(a ,b):
    for i in range(a, b+1):
        yield i**2

for x in squares_generator(a,b):
    print(x)