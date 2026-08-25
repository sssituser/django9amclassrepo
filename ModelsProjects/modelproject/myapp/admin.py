from django.contrib import admin
from myapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model=Employee
admin.site.register(Employee,EmployeeAdmin)


    