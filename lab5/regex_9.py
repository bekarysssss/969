import re

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

string = "BetterCallSaul"
probel = insert_spaces(string)
print("Output:")
print(probel)