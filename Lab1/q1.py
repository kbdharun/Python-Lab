# Q1.Finding all roots of quadratic equation

import math

print("Finding all roots of quadratic Equation")
print("======================================")

a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))

print("The entered values for a,b,c are")
print(a,b,c)
print("\n")

disc = b**2 - 4*a*c
root1 = root2 = 0
if(disc<0):
  print(" No real roots are present in the given quadratic equation.")
  root1 = complex(-b/(2*a), math.sqrt(-disc)/(2*a))
  root2 = complex(-b/(2*a), -math.sqrt(-disc)/(2*a))
  print(root1,root2)
else:
  print("The real roots of the quadratic equation are: ")
  root1 = ((-b)+math.sqrt(disc))/(2*a)
  root2 = ((-b)-math.sqrt(disc))/(2*a)
  print(root1,root2)