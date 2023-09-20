from django.contrib import admin

# Register your models here.

from .models import FruitsInfo,FruitsVendors
#admin.site.register(Employee)
admin.site.register(FruitsInfo)
admin.site.register(FruitsVendors)