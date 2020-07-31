from django.contrib import admin
from testapp.models import Employee

class Employeeadmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

# Register your models here.
admin.site.register(Employee,Employeeadmin)