matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[0][1] = 10
print(matrix)


for row in matrix:
    for element in row:
        print(element, end=' ')
    print()