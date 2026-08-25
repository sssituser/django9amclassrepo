from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["StuId","StuName","StuMarks","StuImg"]
    model=Student
admin.site.register(Student,StudentAdmin)