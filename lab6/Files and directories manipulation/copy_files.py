import os

path1 = input("Vvedite put' k 1 failam:  ")
path2 = input("Vvedite put' k 2 failam:  ")
with open(path1,'r') as first, open(path2,'a') as second:
    for x in first:
        second.write(x)