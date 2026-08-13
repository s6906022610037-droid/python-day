# pop method 
grades = [85,90,78,92,88]
third_grade = grades.pop(2)  # Removes the grade at index 2 (78)
grades.append(third_grade)  # Appends the removed grade to the end of the list
print(f"Grades after popping the third grade: {grades}")