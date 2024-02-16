"""5.Write a Python program to multiply all the items in a dictionary."""


def multiply_all_items(my_dict):
        # Extract numeric values from the dictionary

    numeric_values = [value for value in my_dict.values() if isinstance(value, (int, float))]
    # Initialize the result to 1
    result = 1
    # Multiply each numeric value

    for value in numeric_values:
        result *= value

    return result

def get_user_input_dict():
    # Get the dictionary as a string from user input
    user_input = input("Enter a dictionary (e.g., {'a': 2, 'b': 3}): ")
    
     # Validate the input format
    if not user_input.startswith("{") or not user_input.endswith("}"):
        print("Error: Invalid input format. Please use the format {'a': 1, 'b': 2}")
        return None
 # Convert the input string to a dictionary
    user_dict = eval(user_input)
# Check if the result is a dictionary
    if not isinstance(user_dict, dict):
        print("Error: Invalid input. Please enter a valid dictionary.")
        return None

    return user_dict

user_dict = get_user_input_dict()

if user_dict is not None:
    result = multiply_all_items(user_dict)
    if result is not None:
        print("Result of multiplying all items:", result)


# output:
# if enterd correctly
    """Enter a dictionary (e.g., {'a': 2, 'b': 3}): {'a': 2, 'b': 3}
    Result of multiplying all items: 6 """
# if not
"""Enter a dictionary (e.g., {'a': 2, 'b': 3}): a
    Error: Invalid input format. Please use the format {'a': 1, 'b': 2}"""