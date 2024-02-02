def unique_elements(list):
    unique_list = []
    for el in list:
        if el not in unique_list:
            unique_list.append(el) 
    return unique_list

original_list = [1, 4, 8, 8]
result = unique_elements(original_list)
print(result)