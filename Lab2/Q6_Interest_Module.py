# Q6. Program to calculate the SI and CI (using function and module) - Interest module

'''
 Interest Formulas
===================
  
  Simple Interest  (SI)= p*r*t/(100*12)
  Compound Interest (CI) = (p*((1+r/12)**(12*t)))-p
'''

print('''
Interest Calculator
==================
''')

def simp_intr(p,m,r=11.5):
  return p*r*m/(100*12)
  
def comp_intr(p,m,r=11.5):
  return (p*((1+r/12)**(12*m)))-p