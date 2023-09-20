# Q2.
'''
Create a module called STACK to include the stack (consider tuple) data structure operation
(push,pop,isempty). Include appropriate user defined function for each stack operation in STACK
module. Write a recursive function to reverse the given stack content in another module. Get user input in main
'''

from stack import push,pop,isEmpty

stack = ()
while True:
  ch = int(input("Choices:-\n\n1. Push \n2. Pop \n3. Check empty\n\nEnter choice:"))
  if(ch==1):
    ele = int(input("Enter a number to push: "))
    stack = push(stack,ele)
  elif ch==2:
    stack = pop(stack)
  elif ch==3:
    print("Empty:",isEmpty(stack))
  else: break
  print(stack)