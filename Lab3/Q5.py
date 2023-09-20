# Q5. Merge sort to combine 2 sorted tuples in ascending order

'''
Create two tuples with sorted order. Using merge sort combine these two sorted tuple
elements in an ascending order in final tuple. Write a program to implement this operation
'''

print('''
Merge Sort: Two sorted tuple in ascending order
==============================================
''')

def merge(x,y):
  i = 0
  j=0
  ans = list()
  while i<len(x) and j<len(y):
    if(x[i]<=y[j]):
      ans.append(x[i])
      i+=1
    else:
      ans.append(y[j])
      j+=1

  while i!=len(x):
    ans.append(x[i])
    i+=1
  while j!=len(y):
    ans.append(y[j])
    j+=1
  return ans

x=tuple(list(input("Enter the first sorted array:").split(',')))
y=tuple(input("Enter the second sorted array:").split(','))

ans = merge(x,y)
print("Sorted Tuple:",ans)