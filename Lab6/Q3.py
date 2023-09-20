# Q3

'''
Write a python program to Accept Reg No, Name, Date of Birth for N students and
store them in a list named as Studentdetails. Define a function E-mail creation() to
Create E-mail id as regno@sastra.ac.in using string function and store them in separate
list named as Email. Find the age of students and append the age and Email list in
Studentdetails list. Check whether they are eligible for voting in Indian Constitution and
print the student details in the following format.

Reg No    Name    Date-of-Birth    Age      Email id          Eligibility for voting 
1200213   Naveen   05-06-2003      18    1200213@sastra.ac.in       yes
'''

## Getting user input

from datetime import date
from datetime import time
from datetime import datetime

Studentdetails = []
n = int(input("Enter no of students: "))
for _ in range(n):
  regno = int(input("Enter regno: "))
  name = input("Enter name: ")
  dob = int(input("Enter DOB (DDMMYYYY):"))
  Studentdetails.append([regno, name, dob])

# Creating email id based on regno

def EmailCreation(Studentdetails):
  email = []
  for stud in Studentdetails:
    s = str(stud[0]) + '@sastra.ac.in'
    email.append(s)
  return email

# Determining age from the given DOB and checking Voting Eligibility

def findAge(Studentdetails):
  age = []
  for stud in Studentdetails:
    s = str(stud[2])
    d = int(s[:2])
    month = int(s[2:4])
    year = int(s[4:])
    dateObj = datetime(year, month, d)
    today = datetime.today()
    age.append(int((today - dateObj).days/365))
  return age

def insert(Studentdetails,email,age):
  for i in range(len(Studentdetails)):
    Studentdetails[i].extend((email[i],age[i]))
    if age[i]>=18:
      Studentdetails[i].append("Yes")
    else:
      Studentdetails[i].append("No")

# Create Email ID and find Age
email = EmailCreation(Studentdetails)
age = findAge(Studentdetails)
insert(Studentdetails,email,age)
print(["Reg.no","Name","DOB","Email","Age","Eligibility"])
for i in Studentdetails:
  print(i)