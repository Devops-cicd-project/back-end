from rest_framework import serializers
from .models import Employees, Departments

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        # fields = ('EmployeeId', 
        #           'EmployeeName',
        #           'Department',
        #           'DateOfJoining',
        #           'PhotoFileName'
        #           )
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        # fields = ('DepartmentId', 'DepartmentName') 
        fields = '__all__'
