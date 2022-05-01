# Define 
"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal. 
"""

# Input
"""
The first line contains the integer n, the number of students' records. 
The next n lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.
""" 
n = 3
students = ["Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60"]

# Output
"""
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""
student_marks = {}
for index in range(n):
    name, *line = students[index].split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("student name: ")
notes = student_marks[query_name]

total = 0
for note in notes:
    total += note

print(f"{total/len(notes):.2f}")
