from django.urls import path
from django.urls import re_path as url
from .views import (
    departmentApi, 
    employeeApi, 
    SaveFile
    )

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^department/$', departmentApi),
    url(r'^department/([0-9]+)', departmentApi),

    url(r'^employee/$', employeeApi),
    url(r'^employee/([0-9]+)', employeeApi),

    url(r'^SaveFile', SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)