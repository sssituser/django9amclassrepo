from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):
    StuId = forms.IntegerField()
    StuName = forms.CharField(max_length=40)
    StuMarks = forms.IntegerField()
    StuImg = forms.CharField(max_length=200)
    class Meta:
        model = Student
        fields='__all__'