# Q1

'''
Create a class named EB_amount. It has the data members units_used and bill. Use
inputdtail() member function to get input for unit_used. Upto 200 units 3 rupees per unit, 201
to 500, 4 rupees per and above 500 5.5 rupees per unit are allotted by EB. Calculate the bill
amount in calculate() member function. display the bill amount along with unit used in
printdetail( ) member function. Include constructor to initialize the value as zero to data
members.
'''

print('''
EB Bill Calculator
==================
''')

class EB_amount:
    def __init__(self):
        self.units_consumed = 0
        self.bill = 0

    def inputdetail(self):
        self.units_consumed = int(input("Enter units consumed: "))

    def calculate(self):
        if self.units_consumed <= 200:
            self.bill = self.units_consumed * 3
        elif self.units_consumed <= 500:
            self.bill = 200 * 3 + (self.units_consumed - 200) * 4
        else:
            self.bill = 200 * 3 + 300 * 4 + (self.units_consumed - 500) * 5.5

    def printdetail(self):
        print("Units consumed:", self.units_consumed)
        print("Bill amount:", self.bill)

eb = EB_amount()
eb.inputdetail()
eb.calculate()
eb.printdetail()