import os

path = input("Путь: ")
if os.access(path, os.F_OK):
        os.remove(path)
        print("Done! ")
else: print("File does not exist!")