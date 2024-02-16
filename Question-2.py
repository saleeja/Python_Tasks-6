"""2.Write a Python program to get dictionary keys as a list"""


def keys_as_list(my_dict):
    keys_list = list(my_dict.keys())
    return keys_list


example_dict = {'a': 1, 'b': 2, 'c': 3}


keys_list = keys_as_list(example_dict)

print("Dictionary Keys as List:", keys_list)
