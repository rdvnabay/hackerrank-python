# Task
"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n 
"""

# Input
"""
The first and only line contains the integer, n. 
"""
n = 5

# Output
"""
Print n lines, one corresponding to each i. 
"""
numbers = list(range(0, n))
for number in numbers:
    print(number**2)
