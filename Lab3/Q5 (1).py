# Q4. Matrix type Identification program

'''
Write a Program to check whether the given matrix is symmetric, skew symmetric,diagonal
and identity or NOT using function (Include separate function for each type) using List of
LIST.
'''

print('''
Matrix type determination utility
=================================
''')

def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(i+1, cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_skew_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(i, cols):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True

def is_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i != j and matrix[i][j] != 0:
                return False
    return True

def is_identity(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

# Taking input from the user for the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter the elements of row {i+1}: ").split()))
    matrix.append(row)

# Checking the type of the given matrix using the above functions
if is_identity(matrix):
    print("Given matrix is an Identity matrix")
elif is_diagonal(matrix):
    print("Given matrix is a Diagonal matrix")
elif is_symmetric(matrix):
    print("Given matrix is a Symmetric matrix")
elif is_skew_symmetric(matrix):
    print("Given matrix is a Skew Symmetric matrix")
else:
    print("Given matrix is neither Identity, Diagonal, Symmetric, nor Skew Symmetric")