from itertools import permutations

def print_permutations(string):
    permuted_strings = permutations(string)

    for permuted_string in permuted_strings:
        print(''.join(permuted_string))

user_input = input("")
print_permutations(user_input)