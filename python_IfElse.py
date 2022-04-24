# Task
"""
Given an integer n, perform the following conditional actions:
    If is odd, print Weird
    If is even and in the inclusive range of to, print Not Weird
    If is even and in the inclusive range of to, print Weird
    If is even and greater than , print Not Weird
"""

# Input
"""
A single line containing a positive integer, n.
"""
n = 18

# Output
"""
Print Weird if the number is weird. Otherwise, print Not Weird.
"""

if(n % 2 != 0):
    print("Weird")
else:
    if(n >= 2 and n <= 5):
        print("Not Weird")
    elif(n >= 6 and n <= 20):
        print("Weird")
    elif(n >= 20):
        print("Not Weird")
