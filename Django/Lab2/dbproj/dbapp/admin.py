from django.contrib import admin

# Register your models here.
from .models import Employee, Client
#admin.site.register(Employee) (not needed after first time)
@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display=('empid','empname','empsalary','empaddress','empgrade')
    list_filter=('empsalary','empaddress','empgrade')
    ordering=('empid',)
    search_fields=('empname',)

@admin.register(Client)
class Clientadmin(admin.ModelAdmin):
    list_display=('clid','clname','clquote','cleval','clcountry')
    list_filter=('clquote','cleval','clcountry')
    ordering=('clquote',)
    search_fields=('clname','clid','clcountry')