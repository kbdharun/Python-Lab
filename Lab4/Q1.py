#Q1.
'''
Write a user defined function to find the longest words from the given text file.
'''

list1=[]
with open('test.txt') as f: # default 'rt'
  list1 = (f.read()).split()

max_len = 0
list2 = []
for i in list1:
  if len(i)>max_len:
    max_len = len(i)
    list2.clear()
    list2.append(i)
    
  elif len(i)==max_len:
    list2.append(i)

print("Length of longest word: ", len(list2[0]))
print("The longest word is:")
for i in list2:
  print(i)