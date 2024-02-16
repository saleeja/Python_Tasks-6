"""3.Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys"""

def print_square_dict():
    # Get the range from the user
    start_input = input("Enter the start of the range (integer): ")
    end_input = input("Enter the end of the range (integer): ")

    # Check if both inputs are valid integers
    if start_input.isdigit() and end_input.isdigit():
        start = int(start_input)
        end = int(end_input)

        if start <= end:
            square_dict = {}

            # Create the dictionary with keys as numbers in the specified range
            for key in range(start, end + 1):
                square_dict[key] = key ** 2

            print("Dictionary with Keys and Squares:", square_dict)
        else:
            print("Error: Start of the range should be less than or equal to the end.")
    else:
        print("Error: Please enter valid integers.")

# Call the function
print_square_dict()
