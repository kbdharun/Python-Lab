# Q3. Calculate the sum of matrix elements

'''
Program to calculate the sum value for lower triangular matrix elements and upper
triangular matrix elements of the given matrix using LIST of LIST.
'''

print('''
Matrix Sum Calculation Utility
==============================
''')

def printMatrix(list1):
  for i in range(n):
    for j in range(n):
      print(matrix[i][j], end=' ')
    print()

# Input for Square Matrix

upper = 0
lower = 0
n = int(input("Enter the size of matrix: "))
matrix = list()
for i in range(n):
  list1 = list()
  for j in range(n):
    x = int(input("Enter the element for "+f'({i+1},{j+1})'+" coordinate = "))
    list1.append(x)
    if j < n-i:
      upper+=x
    if j>=n-i-1:
      lower+=x
  matrix.append(list1)

print("The Input Matrix is: ")
printMatrix(list1)


# Sum of elements in matrix
print("Sum of elements in the Upper Triangular Matrix:",upper)
print("Sum of elements in the Lower Triangular Matrix:",lower)