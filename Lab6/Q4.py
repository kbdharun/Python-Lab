# Q4

'''
Create a 2D matrix using LIST of LIST. If the matrix is the square matrix, then
calculate the sum value for lower triangular matrix elements and upper triangular matrix
elements. Otherwise throw an out of bound predefined exception.

Note:-

Sum of lower triangular matrix = diagonal + lower matrix
Sum of upper triangular matrix = diagonal + upper matrix
Sum of lower+upper = (diagonal + lower + upper)+ diagonal = sum of matrix elements + sum of diagonal
'''

## Matrix Creation
m = int(input("Enter no of rows: "))
n = int(input("Enter no of columns: "))
matrix = []
for i in range(m):
  temp = []
  for j in range(n):
    x = int(input(f"Enter element{n*i+j}: "))
    temp.append(x)
  matrix.append(temp)

# Userdefined Index out of bounds exception and sum
if(m!=n):
  raise IndexError("Out of Bounds Exception")
else:
  matrixSum = sum([matrix[y][y] for y in [x for x in range(m)]]); # matrix[0][0]+matrix[1][1]+.. for y in [0 1 2 3 4 5]
  for i in matrix:
    matrixSum+=sum(i)
  print("Matrix sum: ",matrixSum)