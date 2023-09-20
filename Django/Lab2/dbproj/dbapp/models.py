from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=25)
    empsalary = models.IntegerField()
    empgrade = models.CharField(max_length=2)
    empaddress = models.CharField(max_length=50)

class Client(models.Model):
    clid = models.IntegerField()
    clname = models.CharField(max_length=25)
    clquote = models.IntegerField()
    cleval = models.CharField(max_length=2)
    clcountry = models.CharField(max_length=25)
