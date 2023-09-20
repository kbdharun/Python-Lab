# Q1.Program to Calculate Parking Charges of a vehicle

'''
Function to calculate parking charges of a vehicle. Enter the type of vehicle as character (c- car, b- bus, t-
two wheeler..etc) and number of parking hours then calculate the charges as given: bus- 20 rupees per hour, car- 10 rupees per hour, two wheelers- 5 rupees per hour. • Consider function name - pkcharges

• Get the input for vehicle type(as char) and hour value
• pass the character and hour as an argument as and return the final amount
'''

def pkcharges(c,hrs):
  if c=='b':
    return 20*hrs
  elif c == 'c':
    return 10*hrs
  elif c == 't':
    return 5*hrs
  else:
    return -1

print('''
Parking charges calculator
==========================
Note: c = car, b = bike, t = two wheeler
''')
c = input("Enter type of vehicle (c/b/t): ")[0]
hrs = int(input("Enter no of parking hours: "))

price = pkcharges(c,hrs)
if price!=-1:
  print(f"Price: {price} rupees")
else:
  print("Error: Invalid Vehicle type, try again.")