from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model=Student
admin.site.register(Student,StudentAdmin)