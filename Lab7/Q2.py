# Q2

'''
Create a class called SQUARE_ MATRIX with LIST of LIST as the attribute to store
matrix values. Include the following methods in SQUARE_MATRIX class. 
a) Input() - to get input for matrix from the user.
b) Check() - to check whether the given matrix is symmetric, skew symmetric,diagonal
and identity or NOT using function.
c) Display() - print the matrix value.
'''

class SQUARE_MATRIX:
    def __init__(self):
        self.matrix = []

    def input(self):
        n = int(input("Enter number of rows/columns: "))
        print("Enter matrix elements:")
        row = list(map(int, input().split()))
        for i in range(n):
            self.matrix.append(row[3*i:3*(i+1)])

    def check(self):
        n = len(self.matrix)
        
        is_symmetric = True
        is_skew_symmetric = True
        is_diagonal = True
        is_identity = True
        for i in range(n):
            for j in range(n): 
                if self.matrix[i][j] != self.matrix[j][i]:
                    is_symmetric = False
                if i != j and self.matrix[i][j] != -self.matrix[j][i]:
                    is_skew_symmetric = False
                if i != j and self.matrix[i][j] != 0:
                    is_diagonal = False
                if (i == j and self.matrix[i][j] != 1) or (i != j and self.matrix[i][j] != 0):
                    is_identity = False  
        if is_symmetric:
            print("The matrix is symmetric")
        else:
            print("The matrix is not symmetric")
        if is_skew_symmetric:
            print("The matrix is skew-symmetric")
        else:
            print("The matrix is not skew-symmetric")
        if is_diagonal:
            print("The matrix is diagonal")
        else:
            print("The matrix is not diagonal")
        if is_identity:
            print("The matrix is identity")
        else:
            print("The matrix is not identity")

    def display(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                print(self.matrix[i][j], end=" ")
            print()

matrix = SQUARE_MATRIX()
matrix.input()
matrix.display()
matrix.check()