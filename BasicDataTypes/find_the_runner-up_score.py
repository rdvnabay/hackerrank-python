# Define
"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up. 
"""

# Input
"""
The first line contains n. 
The second line contains an array of n integers each separated by a space. 
"""

# Output
"""
Print the runner-up score.
"""

uniqueArr = []
arr = [2, 3, 6, 6, 5]
arr.sort()

for item in arr:
    if item not in uniqueArr:
        uniqueArr.append(item)

print(uniqueArr[-2])
