## Q7. Series calculation using for loop

import math

print('''
Series Calculation
==================
''')

print('''
  a. sin (x) = x - x^3/3! + x^5/5! - ..
  b. cos(x)= 1 - x^2/2! + x^4/4! - ..
  c. e^x = 1+x/1!+x^2/2! + x^3/3! + ..
''')

# Factorial calculation
def fact(n):
  if(n==0 or n==1):
    return 1;
  return n*fact(n-1);

# sin(x) calculation
def sinx_calc(x,no):
  sum = 0
  for i in range(1,no+1):
    sum+= ((-1)**(i-1))*(x**(2*i-1)/fact(2*i-1))
  return sum

n =math.pi/2;
print(sinx_calc(n,50))

# cos(x) calculation
def cosx_calc(x,no):
  sum = 0
  for i in range(1,no+1):
    sum+= ((-1)**(i+1))*(x**(2*i-2) /fact(2*i-2))
  return sum
print(cosx_calc(n,75))

# Exponential calculation

def exp(x,no):
  sum = 0
  for i in range(1,no+1):
    sum+=((x**(i-1))/fact(i-1))
  return sum
print(exp(math.pi,75))