from django.contrib import admin

# Register your models here.
from .models import Employee, Client, Student
#admin.site.register(Employee)
@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display=('empid','empname','empsalary','empaddress')
    list_filter=('empsalary',)
    ordering=('empname',)
    search_fields=('empname',)


@admin.register(Client)
class Clientadmin(admin.ModelAdmin):
    list_display=('clid','clname','clquote','cleval','clcountry')
    list_filter=('clquote','cleval','clcountry')
    ordering=('clquote',)
    search_fields=('clname','clid','clcountry')

admin.site.register(Student)