import re

def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)

string = "CollegedropoutVulturesGraduationDondayYeezus"
split = split_at_uppercase(string)
print("Output:")
print(split)