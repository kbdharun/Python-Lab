# Q5

'''
Create a nested dictionary to maintain N bank customer details (accno, name,balance). 
Read each customer detail from the nested dictionary and store it in a separate list (if the
customer account number greater than 100). if the customer id is less than 100 throw an
predefined exception ‘name Error’ and display
'''

## DICTIONARY CREATION
n = int(input("Enter no of customers: "))
details = {}
for i in range(n):
  details[i] = {}
  details[i]['accno'] = int(input("Enter account number: "))
  details[i]['name'] = input("Enter name: ")
  details[i]['balance'] = float(input("Enter balance: "))

## STORING IN LIST
store = []
for i in details:
  if details[i]['accno']>100:
    store.append([details[i]['accno'],details[i]['name'],details[i]['balance']])
  else:
    try:
      raise NameError
    except:
      print("Exception::")
      print([details[i]['accno'],details[i]['name'],details[i]['balance']])
    finally:
      print("Finally::")
      for i in store:
        print(i)

for i in store:
  print(i)