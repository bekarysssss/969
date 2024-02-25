import re

input = ['ab', 'abbb', 'bbabb', 'ababababa', 'abb', 'bababbabbbbbb']

formul = re.compile(r'ab{2,3}$')

for string in input:
    if formul.search(string):
        print(f"'{string}' match")
    else:
        print(f"'{string}' doesnt match")