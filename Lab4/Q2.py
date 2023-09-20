# Q2.
'''
Write a Python program to read text a file line by line and store it into a list. 
'''
list1 = list()

with open("test.txt") as f:
  line = f.readline()
  while(line):
    line=line.replace("\n","")
    list1.append(line)
    line = f.readline()
    
print(list1)