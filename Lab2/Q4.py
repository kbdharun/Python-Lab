# Q4. Program to Calculate the Volume of Cylinder

'''
Program to compute the volume of a cylinder using a function compute (), with default values 1 for radius
of the cylinder base and 2 for height of the cylinder. Calculate and return the volume of the cylinder, by
calling the function with (input from user) and without arguments.
'''

import math
def compute(r=1,h=2):
  return math.pi*r*r*h

print('''
Volume of Cylinder Calculator
=============================
''')
r = int(input("Enter radius (r) of cylinder: "))
h = int(input("Enter height (h) of cylinder: "))
print("Volume of Cylinder: ",compute(r,h))
print("Volume of Cylinder (default): ",compute())