'''
    File name: seven.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

# Initializing variables...
rows, cols = (int(input()), int(input()))
count = 1
matrix = []

# Fn to print matrix...


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Generating a matrix for given rows and columns...
for r in range(rows):
    column = []
    for c in range(cols):
        column.append(count)
        count = count + 1
    matrix.append(column)

# Printing it out to the user...
printMatrix(matrix)
