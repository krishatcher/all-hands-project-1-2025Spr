"""This module provides functions to generate random strings and store them in different
containers such as lists, sets, and dictionaries."""

# Import the 'random' module, which provides functions for generating random numbers and data
import random
# Import the 'string' module, which provides constants and functions for working with strings
import string
from typing import List, Set, Dict

# Rosa Ruiz Gonzalez

# Function to generate a random string of a given length
def generate_random_string(length: int) -> str:
    """Generate a random string of a given length."""
    # Create lowercase letters a - z, but if you want both use string.ascii_letters
    letters = string.ascii_lowercase
    # Initialize an empty string to store the random string
    random_string = ""
    # Loop length times to create a string of the desired length
    for _ in range(length):
        # Add a randomly chosen letter from letters to random_string
        random_string += random.choice(letters)
    # Return the created random string
    return random_string

# Function to generate a list of random strings
def generate_list_of_random_strings(num_strings: int, string_length: int) -> List[str]:
    """Generate a list of random strings."""
    # Initialize an empty list to store the random strings
    random_list = []
    # Loop num_strings times to create the required number of random strings
    for _ in range(num_strings):
        # Call the function to create random strings of the desired length and add it to the list
        random_list.append(generate_random_string(string_length))
    # Return the list of random strings
    return random_list

# Function to generate a set of random strings (sets do not allow duplicates)
def generate_set_of_random_strings(num_strings: int, string_length: int) -> Set[str]:
    """Generate a set of random strings."""
    # Start an empty set to store the random strings
    random_set = set()
    # Loop until the set contains the required number of unique random strings
    while len(random_set) < num_strings:
        # Create random strings of the desired length and add them to the set
        random_set.add(generate_random_string(string_length))
    # Return the set of random strings
    return random_set

# Function to generate a dictionary of random strings with indices as keys
def generate_dict_of_random_strings(num_strings: int, string_length: int) -> Dict[int, str]:
    """Generate a dictionary of random strings."""
    # Start an empty dictionary to store the random strings
    random_dict = {}
    # Loop num_strings times to create the required number of random strings
    for i in range(num_strings):
        # Create a random string of the desired length and add it to the dictionary
        # The key is the current index i, and the value is the created random string
        random_dict[i] = generate_random_string(string_length)
    return random_dict

# Main part of the script
# This line checks if the script is being run directly (not imported as a module in another script).
if __name__ == "__main__":
    num_strings = 1000  # Number of random strings to generate
    string_length = 5  # Length of each random string

    # Generate containers of random strings
    # Generate a list of random strings
    random_list = generate_list_of_random_strings(num_strings, string_length)
    # Generate a set of random strings
    random_set = generate_set_of_random_strings(num_strings, string_length)
    # Generate a dict of random strings
    random_dict = generate_dict_of_random_strings(num_strings, string_length)

    # Print one random string from each container
    print(f"List of random strings: {random_list[:1]}")
    # Convert the set to a list to allow slicing, but the original set remains unchanged
    print(f"Set of random strings: {list(random_set)[:1]}")
    # Convert the dictionary items to a list to allow slicing, but the original dictionary remains unchanged
    print(f"Dict of random strings: {list(random_dict.items())[:1]}")

# I used three sources for my work. The first source is called Grammarly, which is an AI assistant
# that helps me with my spelling and grammar errors. I typically use it in my comments. The second
# source I used was to understand the module that I utilized to generate random strings,
# specifically `import string`. The third source was copilot, I used to be able to generate the type
# annotation I need in order to meet the class expectation.

# [Grammarly](https://app.grammarly.com)
# [educative](https://www.educative.io/answers/what-is-asciilowercase-constant-in-python)
