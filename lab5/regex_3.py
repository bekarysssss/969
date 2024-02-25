import re

def find_sequences(text):
    formul = r'\b[a-z]+_[a-z]+\b'  
    sequences = re.findall(formul, text)
    return sequences

text = "This sentence written_for regex_3_task and this_task will_be done!"
sequences = find_sequences(text)
print("smth_smth:")
print(sequences)