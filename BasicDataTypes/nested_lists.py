# Define
"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""


# Input
"""
The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade. 
"""
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


# Output
"""
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.
"""

# for _ in range(int(input())):
#     name = input()
#     score = int(input())
#     students.append([name,score])

students.sort(key=lambda x: x[1])

smallestGrade=students[0][1]
secondLowestGrade=0

for student in students:
    if student[1]>smallestGrade:
        secondLowestGrade =student[1]
        break
    
students = list(filter(lambda x: x[1] == secondLowestGrade, students))
students.sort(key=lambda x: x[0])

for student in students:
        print(student[0])
