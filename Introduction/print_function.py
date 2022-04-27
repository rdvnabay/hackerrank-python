# Input
"""
The first line contains an integer n.
"""

# Output
"""
Print the list of integers 1 from through n as a string, without spaces.
"""

def run(n):
    result = ""
    
    for item in range(1, n+1):
        result += str(item)
        
    return result

print(run(4))
