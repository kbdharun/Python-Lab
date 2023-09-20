# Q2. Program to Calculate Standard Deviation of an unknown number of arguments

import math

def stdDeviation(*args):
  x1 = sum(args)/len(args)
  diff = 0
  for x in args:
    diff+=(x-x1)**2
  diff/=len(args)
  return diff**(0.5)
print('''
Standard Deviation Calculator
==========================
''')
print("Standard Deviation =",stdDeviation(1,2,3,4,5,6,7,8,9)) # passing fixed numbers as input