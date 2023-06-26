from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.urls import re_path as url
from rest_framework import routers
from main import views

# routers
router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet, basename='Departments')
router.register(r'employees', views.EmployeetViewSet, basename='Employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
