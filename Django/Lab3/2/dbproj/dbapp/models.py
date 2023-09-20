from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=50)

    def __str__(self):
        return str(self.empid)+" "+self.empname+" "+str(self.empsalary)+" "+self.empaddress

class Client(models.Model):
    clid = models.IntegerField()
    clname = models.CharField(max_length=25)
    clquote = models.IntegerField()
    cleval = models.CharField(max_length=2)
    clcountry = models.CharField(max_length=25)

class Student(models.Model):
    rno=models.IntegerField(default=0,primary_key=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.rno)+" "+self.name