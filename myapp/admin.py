from django.contrib import admin


# Register your models here.
from myapp.models import Employee

admin.site.register(Employee)  # Employee is registered
