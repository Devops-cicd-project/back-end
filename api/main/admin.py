from django.contrib import admin
from .models import Departments, Employees

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('DepartmentId', 'DepartmentName')

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining')
