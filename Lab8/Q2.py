# Q2


'''
Create a class to store the employee details(name,dept,basicsal,GS and NS) in
dictionary(empid is key) as data member. Include the following methods in this class.
a) Read( ) - extract the employee details file and store it in data member. ( if file
does not exist throw an file not found exception).
b) Write ( ) - store N employee details in a file.
c) Getdate ( ) - get N employee details (only name,dept and basicsal) from the
user and store it in data member
d) Display( ) - print the employee detail in table format.
e) Calculate ( ) - calculate NS and GS for each employee by considering
HRA=25%,DA=12% and PF=8%.
'''


class Employee:
    def __init__(self):
        self.__employees = {}


    def read(self):
        try:
            with open('file1.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    emp_details = line.split(',')
                    emp_id = emp_details[0]
                    emp_name = emp_details[1]
                    emp_dept = emp_details[2]
                    emp_basic_sal = float(emp_details[3])
                    self.__employees[emp_id] = {
                        'name': emp_name,
                        'dept': emp_dept,
                        'basic_sal': emp_basic_sal,
                        'GS': 0,
                        'NS': 0
                    }
        except FileNotFoundError:
            print("File not found")


    def write(self, n):
        with open('file1.txt', 'w') as file:
            for i in range(n):
                emp_id = input("Enter employee ID: ")
                emp_name = input("Enter employee name: ")
                emp_dept = input("Enter employee department: ")
                emp_basic_sal = float(input("Enter employee basic salary: "))
                file.write(f"{emp_id},{emp_name},{emp_dept},{emp_basic_sal}\n")
                self.__employees[emp_id] = {
                    'name': emp_name,
                    'dept': emp_dept,
                    'basic_sal': emp_basic_sal,
                    'GS': 0,
                    'NS': 0
                }


    def get_data(self, n):
        for i in range(n):
            emp_id = input("Enter employee ID: ")
            emp_name = input("Enter employee name: ")
            emp_dept = input("Enter employee department: ")
            emp_basic_sal = float(input("Enter employee basic salary: "))
            self.__employees[emp_id] = {
                'name': emp_name,
                'dept': emp_dept,
                'basic_sal': emp_basic_sal,
                'GS': 0,
                'NS': 0
            }


    def calculate(self):
        for emp_id, emp_details in self.__employees.items():
            hra = 0.25 * emp_details['basic_sal']
            da = 0.12 * emp_details['basic_sal']
            pf = 0.08 * emp_details['basic_sal']
            gs = emp_details['basic_sal'] + hra + da
            ns = gs - pf
            self.__employees[emp_id]['GS'] = gs
            self.__employees[emp_id]['NS'] = ns


    def display(self):
        print("{:<10} {:<20} {:<20} {:<10} {:<10}".format("Emp ID", "Name", "Dept", "GS", "NS"))
        print("-" * 70)
        for emp_id, emp_details in self.__employees.items():
            print("{:<10} {:<20} {:<20} {:<10.2f} {:<10.2f}".format(emp_id, emp_details['name'], emp_details['dept'], emp_details['GS'], emp_details['NS']))






# driver code
e = Employee()
e.write(1)
e.read()
e.calculate()
e.display()