# transaction.py
def credit(customers, acc_no, dep_amt):
    for i in range(len(customers)):
        if customers[i][1] == acc_no:
            customers[i][2] += dep_amt
            print("Deposit of {} rupees is successful for account number {}.".format(dep_amt, acc_no))
            print("Updated balance is {} rupees.".format(customers[i][2]))
            return
    print("ERROR: Account number not found.")

def debit(customers, acc_no, debit_amount):
    for i in range(len(customers)):
        if customers[i][1] == acc_no:
            if debit_amount <= customers[i][2]:
                customers[i][2] -= debit_amount
                print("Withdrawal of {} rupees is successful for account number {}.".format(debit_amount, acc_no))
                print("Updated balance is {} rupees.".format(customers[i][2]))
                return
            else:
                print("ERROR: Insufficient balance.")
                return
    print("ERROR: Account number not found.")

def ordered(customers):
    n = len(customers)
    for i in range(n-1):
        for j in range(n-i-1):
            if customers[j][2] > customers[j+1][2]:
                customers[j], customers[j+1] = customers[j+1], customers[j]
    print("Sorted customer details based on balance amount:")
    for i in range(n):
        print("{}. Name: {}, Account Number: {}, Balance: {} rupees.".format(i+1, customers[i][0], customers[i][1], customers[i][2]))
