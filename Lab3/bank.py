# Q6. Bank Management Program with 1 imported modules
# bank.py
'''
Write a Python program to perform a Bank Transaction by including the following operation
a) In BANK module, create a List of List to maintain N customer details. For each customer
get the input for Name, Account_number and balance amount from the user. Bank
transaction operations are performed using the functions in Transaction module.

b) Create another module called TRANSACTION with three user defined function
CREDIT( ), DEBIT ( ) and ORDERED( ). 

c) CREDIT( ) function is used to perform the deposit operation by 
receiving list of customers details, Account_no and deposit amount as the arguments. 
Deposit operation is performed based on Account_no (receiving argument). 

d) DEBIT( ) function performs the withdraw operation by receiving list of customers details, Account_no and debit amount as the arguments. Based on receiving Account_no
withdraw operation is performed. ( Note if debit amount is less than balance amount then
withdraw operation is performed otherwise no changes in the balance amount).

e) ORDERED( ) function sort the N customer details in ascending order based on balance
amount of the customer (don’t use any built-in function). Receive N customer details as
an argument. Print the updated customer details of each operation within the corresponding user defined
function itself.
'''

print('''
Bank Management Utility
=======================
''')

from transaction import credit, debit, ordered

# Creating a list of lists to maintain customer details
customers = []
n = int(input("Enter the number of customers: "))
for i in range(n):
    name = input("Enter the name of customer {}: ".format(i+1))
    acc_no = input("Enter the account number of customer {}: ".format(i+1))
    balance = float(input("Enter the balance amount of customer {}: ".format(i+1)))
    customers.append([name, acc_no, balance])

# Performing bank transactions using the functions in Transaction module
print("1. Deposit")
print("2. Withdraw")
print("3. Sort by balance")
choice = int(input("Enter your choice: "))
if choice == 1:
    acc_no = input("Enter the account number: ")
    dep_amt = float(input("Enter the deposit amount: "))
    credit(customers, acc_no, dep_amt)
elif choice == 2:
    acc_no = input("Enter the account number: ")
    debit_amount = float(input("Enter the withdraw amount: "))
    debit(customers, acc_no, debit_amount)
elif choice == 3:
    ordered(customers)
