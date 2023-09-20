# Q5. Program for Net Salary Calculation for N employees

'''
Program to calculate Net Salary of N employees using List with Nested function. 
Store N employee basic pay (to be entered by the user) in LIST data type. 
Assume HRA=10% of the basic pay, TA=5% of basic pay and PF as 4% of basic pay.
Include a calculation( ) user defined function to calculate the final net
salary by receiving basic pay list as the parameter. 
Assign HRA,TA and PF value in calculation function. 
Also initialize empty net-salary LIST variable. 
Include another user defined function called net_sal()
inside calculation() function to calculate each employee net salary 
and store it in net-salary
'''
print('''
Net Salary Calculation Utility
=============================
''')

def solve():
  def InputList():
    list1 = list()
    n = int(input("Enter no of employees: "))
    for i in range(n):
      x = int(input("Enter the basic pay: "))
      list1.append(x)
    return list1

  def calculation(list1):
    def net_sal(HRA, TA, PF):
      net = HRA + TA - PF
      return net
      
    list2 = []
    for basic in list1:
      HRA = 10*basic/100
      TA = 5*basic/100
      PF = 4*basic/100
      list2.append(net_sal(HRA, TA, PF))
    return list2
    
  list1 = InputList()
  return calculation(list1)

list2 = solve()
print("\nNet Salary of Employees: ")
for i in range(len(list2)):
  print(f"Employee {i+1}: {list2[i]}")
