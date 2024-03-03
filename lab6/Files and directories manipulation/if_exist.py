import os

path = input("Путь: ")
print('Exist:', os.access(path, os.F_OK))
if os.access(path, os.F_OK):
    print("Filename and directory: ")
    print([name for name in os.listdir(path)]) 
else:
    print("[]")