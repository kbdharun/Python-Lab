# Q3. To calculate the Gross salary of employee

print("Employee Salary Calculator")
print("==========================")
basic = int(input("Enter basic salary: "))

if(basic <= 10000):
  HRA = 20*basic/100
  DA = 80*basic/100
elif(basic <= 20000):
  HRA = 25*basic/100
  DA = 90*basic/100
else:
  HRA = 30*basic/100
  DA = 95*basic/100

gross = basic+HRA+DA
print("\nBasic:",basic," HRA:",HRA," DA:",DA)
print("\nRequired Gross salary:",gross,"\n")