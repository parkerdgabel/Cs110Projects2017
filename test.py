def myster2d(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0]) - 1):
            if matrix[r][c + 1] > matrix[r][c]:
                matrix[r][c] = matrix[r][c + 1]


numbers = [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
myster2d(numbers)
print(numbers)
