"""8.Create a function that takes a string and returns a dictionary where keys are letters, and values are the number of times each letter appears in the string """

def count_letters(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

def get_user_input():
    while True:
        user_input = input("Enter a string: ")

        # Check if the input contains a number
        if any(char.isdigit() for char in user_input):
            print("The string should not contain numbers.")
            user_choice = input("Do you want to check another string (yes/no)? ")
            if user_choice != 'yes':
                print("Exiting.")
                return None

        else:
            return user_input


user_string = get_user_input()

if user_string is not None:
    # Call the function to count letters
    result_dict = count_letters(user_string)

    # Print the result
    print(f"Letter count in '{user_string}' is {result_dict}.")
