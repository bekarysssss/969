import os

path1 = input("Путь1: ")
path2 = input("Путь2: ")
with open(path1,'r') as first, open(path2,'a') as second:
    for x in first:
        second.write(x)