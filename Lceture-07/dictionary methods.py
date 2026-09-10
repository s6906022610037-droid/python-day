student = {'name' : 'Alice', 'age': 26, 'major': 'Computer Science'}
print(student.keys())

print(student.values())
print(student.items())
print(student.get('name'))
print(student.get('grade', 'Not Found'))
print(student.pop('major'))
print(student)

last_student = student.popitem()
print(last_student)
print(student)

student.clear()
print(student)
