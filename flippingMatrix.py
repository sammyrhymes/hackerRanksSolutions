def flippingMatrix(matrix):
    sum = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n // 2):
        for j in range(m // 2):
            cur = matrix[i][j]
            right = matrix[i][m - j - 1]
            down = matrix[n - i - 1][j]
            diag = matrix[n - i - 1][m - j - 1]
            ans = max(cur, right, down, diag)
            sum += ans
    return sum

def accept_matrix():
    # Prompt the user to input the dimensions of the matrix
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    # Initialize an empty matrix
    matrix = []

    # Prompt the user to input the elements of the matrix
    print("Enter the elements of the matrix (row-wise):")
    for i in range(n):
        row = list(map(int, input().split()))[:m]
        matrix.append(row)

    return matrix

# Example usage:
matrix = accept_matrix()
print("Input matrix:")
for row in matrix:
    print(row)

result = flippingMatrix(matrix)
print(f'solution is {result}')