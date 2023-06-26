from django.db import models


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId = models.AutoField(
        'Employee Id', 
        primary_key=True, 
        default=None
        )
    EmployeeName = models.CharField(
        'Employee Name', 
        max_length=100
        )
    Department = models.CharField(
        'Department', 
        max_length=100
        )
    DateOfJoining = models.DateField('Date of Joining')
    PhotoFileName = models.CharField(
        'Photo File Name', 
        max_length=100, 
        default=None
        )
    
 
