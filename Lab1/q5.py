# Q5.  To print the number of +ve, -ve and 0. & Find the sum and average of given numbers

print('''
Program to print +ve, -ve and 0es and
finding the sum and avg of given data
=====================================
''')
n = int(input("Enter number of elements: "))
numbers = list()
neg = zero = pos = sum = 0

for i in range(n):
  x = int(input("Enter elements: "))
  if(x<0):
    neg+=1
  elif(x==0):
    zero+=1
  else :
    pos+=1
  sum+=x

else:
  print("Number of positive numbers:",pos)
  print("Number of negative numbers:",neg)
  print("Number of zeros:",zero)
  print("Sum of all the numbers:",sum)
  print("Average of all numbers:",sum/n)