# Q1. Inserting an element using lists

'''
Assume list consists of set of elements in ascending order. Write a program to insert an
element in the list based on data. (using insert( ) method)
'''
print('''
Insert Elements into a list
===========================
''')
n = int(input("Enter the number of elements: "))
list = []
for i in range(n):
  print(f"Enter element --> {i+1}: ")
  list.append(int(input()))

print(list)
ele = int(input("Enter the element to insert: "))
index = -1;
for i in range(len(list)):
  if list[i]<ele:
    index=i;
  else:
    break;

list.insert(index+1,ele)
print(list)