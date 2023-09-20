# Q3

'''
Create a class called Employee with the data members emp_id, name, designation and
salary(private). It contains the member functions to get details of employee and display them.
Get the necessary details using member functions and display the employee details with their
salary according to the given data. (include constructor to initialize the salary value as zero.).
Include an user defined function to calculate the net salary and gross salary of an employee by
receiving Employee class object,DA,HRA and PF amount as the parameter.
'''

# Employee class
print('''
Employee Salary Calculator
===========================
''')
class Employee:
  def __init__(self):
    self.__emp_id = 0
    self.__name = ""
    self.__desig = ""
    self.__salary = 0

  def get_details(self):
    self.__emp_id = int(input("Enter Employee ID: ")) # chk output
    self.__name = input("Enter name: ")
    self.__desig = input("Enter designation: ")
    self.__salary = float(input("Enter salary: "))

  def display(self):
    print()
    print('''
EMPLOYEE DETAILS
=================
''')
    print(f"Employee ID: {self.__emp_id}")
    print(f"Employee name: {self.__name}")
    print(f"Employee designation: {self.__desig}")
    print(f"Employee salary: {self.__salary}")

  def getSalary(self):
    return self.__salary

# Net,gross salary calculation
def calcSalDetails(emp_obj, DA, HRA, PF):
    salary = emp_obj.getSalary()
    net_salary = salary-PF+DA+HRA    # Adding allowances, reducing taxes and PF
    gross_salary = net_salary + PF   # Including taxes
    print(f"Net Salary: {net_salary}")
    print(f"Gross salary: {gross_salary}")


emp = Employee()
emp.get_details()
emp.display()

DA = 50
HRA = 25
PF = 500

calcSalDetails(emp, DA, HRA, PF)
