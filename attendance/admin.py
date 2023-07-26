from django.contrib import admin
from .models import Employees
admin.site.register(Employees)
from .models import Attendance
admin.site.register(Attendance)
