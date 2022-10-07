"""Strengmanipulasjon. Innlevering 6"""

def find_substring_index(str_1, str_2):
    index_list = []
    string_to_find = str_1.lower()
    search_string = str_2.lower()
    index = search_string.find(string_to_find)
    while index != -1:
        index_list.append(index)
        index = search_string.find(string_to_find, index+1)
    return index_list

def change_substring(str_1, str_2, str_3):
    index_list = find_substring_index(str_1, str_2)
    final_string = list(str_2)
    for i, index in enumerate(index_list):
        for _ in enumerate(str_1):
            final_string.pop(index+i*(len(str_3)-len(str_1)))
        for j, letter in enumerate(str_3):
            final_string.insert(index+j+i*(len(str_3)-len(str_1)), letter)
    final_string = "".join(final_string)
    return final_string


STRING_1 = "bc"
STRING_2 = "abc abcabc abcabc"
STRING_3 = "A"

print(find_substring_index(STRING_1, STRING_2))
print(change_substring(STRING_1, STRING_2, STRING_3))
