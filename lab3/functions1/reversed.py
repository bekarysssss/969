def reverse_word(str):
    word = str.split()
    reversed_word = reversed(word)

    reversed_sentence = ' '.join(reversed_word)
    return reversed_sentence

user_input = input()
result = reverse_word(user_input)
print(result)