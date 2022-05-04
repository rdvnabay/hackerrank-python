import textwrap

# Function Description
"""
wrap has the following parameters:

    string string: a long string
    int max_width: the width to wrap to
    
    Returns
    string: a single string with newline characters ('\n') where the breaks should be
"""

# Solution
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    result = wrapper.wrap(text=string)
    return "\n".join(result)


output = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
print(output) 

# Output 
"""
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
