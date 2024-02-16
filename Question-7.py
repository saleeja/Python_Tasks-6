"""7.Write a Python program to Delete a list of keys from a dictionary"""


def delete_keys(my_dict, keys_to_delete):
    # Check if the keys_to_delete are in the dictionary
    for key in keys_to_delete:
        if key not in my_dict:
            print(f"Error: Key '{key}' does not exist in the dictionary.")
            return None

    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del my_dict[key]

    return my_dict

existing_dict = {'a': 1, 'b': 2, 'c': 3 , 'g': 8, 's': 4, 'z': 0}

# Ask the user for keys to delete
keys_to_delete = input("Enter keys to delete (comma-separated): ").split(',')

result_dict = delete_keys(existing_dict, keys_to_delete)

if result_dict is not None:
    print("Dictionary after deletion:", result_dict)
    print("Keys successfully deleted.")

# output:
# if key exist
"""Enter keys to delete (comma-separated): a
Dictionary after deletion: {'b': 2, 'c': 3}
Keys successfully deleted."""

# if not exist
"""Enter keys to delete (comma-separated): d
Error: Key 'd' does not exist in the dictionary."""