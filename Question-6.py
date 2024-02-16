"""6.Write a Python program to get the maximum and minimum values of a dictionary"""


def find_max_min_values(my_dict):
    # Find the maximum and minimum values
    max_value = max(my_dict.values())
    min_value = min(my_dict.values())

    return max_value, min_value

example_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}

max_val, min_val = find_max_min_values(example_dict)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
