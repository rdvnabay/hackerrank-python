# Task
"""
Task

You are given a string S.
Your task is to find out if the string S contains:
alphanumeric characters, 
alphabetical characters, 
digits, 
lowercase and 
uppercase characters. 
"""


# Input 
"""
A single line containing a string S.
"""
s = "qA2"


# Output 
"""
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
"""

is_alpha_numeric = any(chracter.isalnum() for chracter in s)
is_alpha = any(character.isalpha() for character in s)
is_numeric = any(character.isnumeric() for character in s)
is_lower=any(character.islower() for character in s)
is_upper=any(character.isupper() for character in s)

print(is_alpha_numeric)
print(is_alpha)
print(is_numeric)
print(is_lower)
print(is_upper)
