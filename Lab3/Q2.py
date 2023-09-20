# Q2. Program to remove duplicate entries in an list

'''
Program to remove duplicate elements from the given list of values using a function. Create
a function called rem_dup( ) to remove duplicate elements. Pass list values as an argument
to the function. Print the final updated list values outside the function. (don’t return
anything from the function)
'''

print('''
Duplicate Entries Purge Utility for Lists
=========================================
''')

# Remove duplicates using rem_dep user defined function
def rem_dup(list1):
  i = 0;
  while(i<len(list1)):
    j = i+1
    while(j<len(list1)):
      if list1[i]==list1[j]:
        del list1[j]
      else:
        j+=1
    else:
      i+=1

n = int(input("Enter the number of elements: "))
list1 = list()
for i in range(n):
  x = int(input(f"Enter element --> {i+1}: "))
  list1.append(x)
print("List before removing duplicates: ", list1)

rem_dup(list1)
print("List after removing duplicates: ", list1)