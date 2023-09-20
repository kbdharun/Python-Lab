# Q5

'''
Create a nested dictionary to store N student details such as rno,name,dept,marks(list of 5
subjects),credits(list of 5 subjcets). Assum rno is the key value in outer dictionary. Calculate
each student SGPA and CGPA and update for each student in nested dictionary.
'''

print('''
CGPA and SGPA Calculation Program
=================================
''')

class Student:
    def __init__(self, name, dept, marks, credits):
        self.name = name
        self.dept = dept
        self.marks = marks
        self.credits = credits
        self.sgpa = self.calculate_sgpa()
        self.cgpa = None

    def calculate_sgpa(self):
        total_marks = sum(self.marks)
        total_credits = sum(self.credits)
        sgpa = total_marks / total_credits
        return round(sgpa, 2)

class StudentRecord:
    def __init__(self):
        self.students = {}

    def add_student(self, rno, name, dept, marks, credits):
        self.students[rno] = Student(name, dept, marks, credits)

    def calculate_cgpa(self):
        total_sgpa = 0
        total_credits = 0
        for rno, student in self.students.items():
            total_sgpa += student.sgpa * sum(student.credits)
            total_credits += sum(student.credits)
            student.cgpa = round(total_sgpa / total_credits, 2)

    def print_details(self):
        for rno, student in self.students.items():
            print(f"Roll No.: {rno}")
            print(f"Name: {student.name}")
            print(f"Department: {student.dept}")
            print(f"Marks: {student.marks}")
            print(f"Credits: {student.credits}")
            print(f"SGPA: {student.sgpa}")
            print(f"CGPA: {student.cgpa}")
            print("")

if __name__ == "__main__":
    record = StudentRecord()
    n = int(input("Enter number of students: "))
    for i in range(n):
        rno = input(f"Enter roll number for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        dept = input(f"Enter department for student {i+1}: ")
        marks = []
        credits = []
        for j in range(5):
            marks.append(int(input(f"Enter marks for subject {j+1} of student {i+1}: ")))
            credits.append(int(input(f"Enter credits for subject {j+1} of student {i+1}: ")))
        record.add_student(rno, name, dept, marks, credits)
    record.calculate_cgpa()
    record.print_details()