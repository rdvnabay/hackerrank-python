# Task
"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 
"""


# Input 
"""
The one line contains a string consisting of space separated words. 
"""


# Function Description
"""
split_and_join has the following parameters:
    string line: a string of space-separated words
    
Returns
    string: the resulting string
"""
def split_and_join(line):
    return "-".join(line.split())
 
 
output=split_and_join("this is a string")
print(output) # this-is-a-string