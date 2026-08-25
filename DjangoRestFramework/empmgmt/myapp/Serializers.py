from rest_framework import serializers
from myapp.models import Employoee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employoee
        fields ='__all__'