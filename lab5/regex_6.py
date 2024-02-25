import re

def replace_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)

text = "Test sentence. We need, to know how its works."
replace = replace_with_colon(text)
print("Modified text:")
print(replace)