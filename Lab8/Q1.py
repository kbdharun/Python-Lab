# Q1

'''
Create a class called STACK with list as the data member(private) . Include the
following methods in stack class:
a) Push() - insert the parameter in List data member at the end.
b) Pop() - remove the top element from the list . 
Write a program to verify that whether in the given mathematical infix expression
parenthesis or matched or not.
'''

class STACK:

  def __init__(self):
    self.__stack = []

  def push(self, ele):
    self.__stack.append(ele)

  def pop(self):
    try:
      ele = self.__stack[-1]
      self.__stack.pop()
    except IndexError:
      return 0
    else:
      return ele

  def display(self):
    print(self.__stack)


def paranMatch(expr):
  stack = STACK()
  flag = 0
  for i in range(len(expr)):
    stack.display()
    if expr[i] == ")":
      s = stack.pop()
      stack.display()
      while (i > 0 and s != '('):
        s = stack.pop()
        if s!='(' and i==1:
          print("Not matched")
          flag = 1
          break
        stack.display()
        i -= 1
    else:
      stack.push(expr[i])
      stack.display()
  if stack.pop() == 0:
    if flag==0:
      print("Matched") 
  else:
    if flag==0:
      print("Not matched") 

# Passing the expression
input_list = ['(((a+b)+c)*d)', '(((a+b)*c)+d', '((a*b)+c)*d)']
for i in input_list:
  paranMatch(i)
