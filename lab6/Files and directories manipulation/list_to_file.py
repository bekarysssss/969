import os

path = input("Vvedite put' k failam:  ")
list = input("Vvedite list:  ").split()
with open(path, 'w') as file:
    for x in list:
        file.write("%s\n" % x)