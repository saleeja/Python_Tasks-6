"""1.Write a Python program to merge two Python dictionaries."""
# simple using update method:
# Create the first dictionary 'dict1' and 'dict2' with key-value pairs.
# dict1 = {'a': 100, 'b': 200, 'c':700}
# dict2 = {'x': 300, 'y': 400}

# # Merge d2 into d1
# dict1.update(dict2)

# print("The Merged Dictionary:",dict1)

# ------------------------------------------------------------------------------------------------------------------
# another method:

def merge_dictionary(dict1, dict2):
    # Create a copy of the first dictionary to avoid modifying it
    merge_dictionary = dict1.copy()
    # Here checking is the value is overwritting or not if overwrite giving message about the overwrite
    for key, value in dict2.items():
        # Check if the key already exists in the merged dictionary
        if key in merge_dictionary:
            print(f"Key '{key}' is overwritten with value {value}")
        
        # Update the merged dictionary with the key-value pair from the second dictionary
        merge_dictionary[key] = value
    return merge_dictionary

dict1 = {'a': 8, 'b': 25}
dict2 = {'b': 18, 'c': 44}

result_dict = merge_dictionary(dict1, dict2)

print("Merged Dictionary:", result_dict)

# output:
# Key 'b' is overwritten with value 18
# Merged Dictionary: {'a': 1, 'b': 3, 'c': 4}