# Task
"""
Task
Given an integer, n, and n space-separated integers as input,
create a tuple, t, of those n integers. Then compute and print the result of hash(t). 
"""

# Input
"""
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t. 
"""
n = 2
integer_list = [1,2]

# Output
"""
Print the result of hash(t). 
"""
print(hash(tuple(integer_list)))
