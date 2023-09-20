# Q5. Merge sort to combine 2 sorted tuples in ascending order

'''
Create two tuples with sorted order. Using merge sort combine these two sorted tuple
elements in an ascending order in final tuple. Write a program to implement this operation
'''

print('''
Merge Sort: Two sorted tuple in ascending order
==============================================
''')
x=list(input("Enter the first sorted array:"))
y=list(input("Enter the second sorted array:"))

merge = x+y
merge.sort()
print("Sorted Tuple:",merge)