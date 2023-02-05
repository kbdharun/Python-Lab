# Q2.To check whether the triangle is an equilateral, isosceles or scalene

print('Program to check the type of triange')
print('===================================')
print('''
This program checks for the type of triangle based on given input:
  - If all three sides are equal  ==>  Equilateral triangle
  - If any two sides are equal    ==>  Isosceles triangle
  - If none are equal             ==>  Scalene triangle
    Note: a,b,c are sides of a triangle
''')

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a==b==c):
  print("It is an Equilateral Triangle")
elif(a==b or b==c or a==c):
  print("It is an Isosceles Triangle")
else:
  print("It is a Scalene Triangle")