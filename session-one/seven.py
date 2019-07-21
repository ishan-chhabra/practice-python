

rows, cols = (int(input()), int(input()))
count = 1


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


matrix = []

for r in range(rows):
    column = []
    for c in range(cols):
        column.append(count)
        count = count + 1
    matrix.append(column)

printMatrix(matrix)
