import re

def match_a_b(string):
    formul = r'a.*b$'
    return bool(re.match(formul, string))

input = ['acb', 'abb', 'ab', 'abc', 'acbcb', 'abdb', 'acbde']
for string in input:
    print(f"'{string}' matches the pattern: {match_a_b(string)}")