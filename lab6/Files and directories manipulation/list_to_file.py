import os

path = input("Путь: ")
list = input("List: ").split()
with open(path, 'w') as file:
    for x in list:
        file.write("%s\n" % x)