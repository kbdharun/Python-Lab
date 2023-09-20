from django.contrib import admin

# Register your models here.
from .models import Student
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stufee','stuaddress','stumobile','stubgrp')
    list_filter=('stufee','stubgrp',)
    ordering=('stuid',)
    search_fields=('stuid','stuname','stuaddress','stugrp')