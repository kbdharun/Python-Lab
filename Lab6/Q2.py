# Q2

'''
Create a STR_FNC(arg) which accepts string as an argument. The function must
satisfy the following constraints. 

(i) If argument string length is less than 2 then print insufficient length to process. 

(ii) If argument string length is equal to 2 then print the string with 'ing'

[ex: 'ab' -> ' abing' ]

(iii) If argument string length is equal to 3 then print the string last character with 'ed'

[ex: 'abc' -> 'ced' ]

(iv) If argument string length is more than 3 then print the first two characters with last
two characters. [ex: 'abcde' -> 'abde']
'''

# STR_FNC functon with the given arguments
def STR_FNC(arg):
  if(len(arg)<2):
    print('Insufficient length to process')
  elif(len(arg)==2):
    print(arg+'ing')
  elif(len(arg)==3):
    print(arg[-1]+'ed')
  else:
    print(arg[:2]+arg[-2:])


# User input
s = input("Enter string: ")
STR_FNC(s)