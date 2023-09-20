# Q1

'''
Create three separate three list such as sname, rollno and CGPA in order to 
store the student name, rollno and CGPA respectively for N students. Write a python 
code to print each student name along with rollno and CGPA using string methods.
'''

N = int(input("Enter the number of students: "))

# Create empty lists
sname = []
rollno = []
cgpa = []

# Get user input
for i in range(N):
    sname.append(input("Enter the student's name: "))
    rollno.append(input("Enter roll number: "))
    cgpa.append(input("Enter CGPA: "))

# Print the value using string method
for i,j,k in zip(sname,rollno,cgpa):
  s = "Student Name: "+i+", His roll number: "+str(j)+" and CGPA="+str(k)
  print(s)