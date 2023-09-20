# Q3.

'''
Write a function RevText() to read a text file “ Story.txt “ and Print only word starting with ‘I’ in
reverse order . Example: If value in text file is: INDIA IS MY COUNTRY Output will be: AIDNI SI MY
COUNTRY
'''

list1 = list()
with open('test.txt') as f:
  list1 = f.read().split()

for i in range(len(list1)):
  if list1[i][0].upper() == 'I':
    list1[i]=list1[i][::-1]

for i in list1:
  print(i, end = ' ')