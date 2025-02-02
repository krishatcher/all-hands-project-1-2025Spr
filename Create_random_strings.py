import random # Import the 'random' module, which provides functions for generating random numbers and data
import string # Import the 'string' module, which provides constants and functions for working with strings

# Rosa Ruiz Gonzalez

# Function to generate a random string of a given length
def generate_random_string(length):
    # Create lowercase letters a - z, but if you want both used string.ascii_letters
    letters = string.ascii_lowercase
    # Initialize an empty string to store the random string
    random_string = ""
    # loop length times to create a sting of a want it length
    for i in range(length):
        # add a random chosen letter from letters to random_string
        random_string += random.choice(letters)
    # return the create it random string
    return random_string

# Function to generate a list of random strings
def generate_list_of_random_strings(num_strings, string_length):
    # initialize an empty list to store the random strings
    random_list = []
    # loop num_strings times to create the required number of random strings
    for _ in range(num_strings):
        # call the fuction to create random strings of the want it length and add it to the list
        random_list.append(generate_random_string(string_length))
    # return the list of random strings
    return random_list

# Function to generate a set of random strings (sets do not allow duplicates)
def generate_set_of_random_strings(num_strings, string_length):
    # Start an empty set to store the random strings
    random_set = set()
    # loop until the set contains the required numbers of unique random strings
    while len(random_set) < num_strings:
        # create random strings of the want ot length and add it to the set
        random_set.add(generate_random_string(string_length))
    # return the set of random strings
    return random_set

# Function to generate a dictionary of random strings with indices as keys
def generate_dict_of_random_strings(num_strings, string_length):
    # start an empty dictionary to store the random stings
    random_dict = {}
    # loop num_strings times to create the required numbers of random strings
    for i in range(num_strings):
        # create a random string of the want it length and add it to the dictionary
        # the key is the current index i, and the value is the created random string
        random_dict[i] = generate_random_string(string_length)
    return random_dict

# Main part of the script
# This line checks if the script is being run directly (not imported as a module in another script).
if __name__ == "__main__":
    num_strings = 1000  # Number of random strings to generate
    string_length = 5  # Length of each random string

    # Generate containers of random strings
    # genarte a list of random strings
    random_list = generate_list_of_random_strings(num_strings, string_length)
    # generate a set of random strings
    random_set = generate_set_of_random_strings(num_strings, string_length)
    # generate a dict of random strings
    random_dict = generate_dict_of_random_strings(num_strings, string_length)

    # Print the one random strings from each container
    print(f"List of random strings: {random_list[:1]}")
    # Convert the set to a list to allow slicing, but the original set remains unchanged
    print(f"Set of random strings: {list(random_set)[:1]}")
    # Convert the dictionary items to a list to allow slicing, but the original dictionary remains unchanged
    print(f"Dict of random strings: {list(random_dict.items())[:1]}")