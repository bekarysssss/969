def snake_to_camel(snake_case):
    return ''.join(word.capitalize() for word in snake_case.split('_'))

snake_case_string = "Two_Cookies_To_Mister_Supa"
camel_case_string = snake_to_camel(snake_case_string)
print("Camelcase:")
print(camel_case_string)