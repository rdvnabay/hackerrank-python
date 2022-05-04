# Task
"""
Read a given string, change the character at a given index and then print the modified string. 
"""

# Function Description
"""
mutate_string has the following parameters:

    string string: the string to change
    int position: the index to insert the character at
    string character: the character to insert
    
    Returns
    string: the altered string

"""

# Solution
def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = "".join(string)
    return string


output = mutate_string("abracadabra", 5, "k")
print(output)  # abrackdabra
