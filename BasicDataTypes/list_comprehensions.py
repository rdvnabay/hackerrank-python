
# Input
"""
Four integers x,y,z and n, each on a separate line. 
"""
x = 1
y = 1
z = 2
n = 3

# Output
"""
Print the list in lexicographic increasing order.
"""
output = []

listOne = [i for i in range(x+1)]
listTwo = [j for j in range(y+1)]
listThree = [k for k in range(z+1)]

for i in listOne:
    for j in listTwo:
        for k in listThree:
            if (i+j+k != 3):
                output.append([i, j, k])

print(output)
