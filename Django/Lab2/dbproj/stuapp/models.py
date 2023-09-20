from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=25)
    stufee = models.IntegerField()
    stuaddress = models.CharField(max_length=50)
    stumobile = models.CharField(max_length=20)
    stubgrp = models.CharField(max_length=3)