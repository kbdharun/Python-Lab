# Q4 To calculate Grade and Percentage from 5 subject marks

print("Percentage and Grade calculator")
print("===============================")
print('''
------Subjects-------
Subject 1 = Physics
Subject 2 = Chemistry
Subject 3 = Biology
Subject 4 = Mathematics
Subject 5 = Computer
''')

marks = list()
for i in range(5):
  m = int(input(f"Enter the marks of Subject {i+1}: "))
  marks.append(m)

percentage = sum(marks)/5
if(percentage>=90):
  print("\nGrade: A","\nPercentage:",percentage)
elif(percentage>=80):
  print("\nGrade: B","\nPercentage:",percentage)
elif(percentage>=70):
  print("\nGrade: C","\nPercentage:",percentage)
elif(percentage>=60):
  print("\nGrade: D","\nPercentage:",percentage)
elif(percentage>=40):
  print("\nGrade: E","\nPercentage:",percentage)
else:
  print("Grade F","\nPercentage:",percentage)

