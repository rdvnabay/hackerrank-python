# Task
"""
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function. 
"""

# Input
"""
Read year, the year to test. 
"""

# Output
"""
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
"""


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 100 == 0) and (year % 400 != 0):
        leap = False
    elif (year % 4 == 0):
        leap = True

    return leap


result = is_leap(2002)
print(result)
