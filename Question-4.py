"""4.Write a Python program to sum all the items in a dictionary."""


def sum_of_all():
    # Get the dictionary from the user as a string
    user_input = input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): ")

    if not user_input.startswith("{") or not user_input.endswith("}"):
        # print("Error: Invalid input format. Please use the format {'a': 1, 'b': 2}")
        return print("Error: Invalid input format. Please use the format {'a': 1, 'b': 2}")

    # Convert the input string to a dictionary
    user_dict = eval(user_input)


    # Calculate the sum of all values in the dictionary
    total_sum = sum(user_dict.values())

    # Print the result
    print("Sum of all items in the dictionary:", total_sum)


sum_of_all()
user_choice = input("Do you want to continue (yes/no)? ")

if user_choice == 'no':
    print("Thank you for using the program. Exiting.")
else:
    print(sum_of_all())
