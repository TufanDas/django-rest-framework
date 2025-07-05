from rest_framework import serializers
from students.models import Students
from employees.models import Employees


# Importing Django REST Framework's ModelSerializer to easily convert model instances to JSON and vice versa
from rest_framework import serializers

# Serializer for the Students model
# This will handle converting Student model objects into JSON format and validating input data
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students  # Tells the serializer which model to base the serialization on
        fields = "__all__"  # Automatically include all fields from the Students model

# Serializer for the Employees model
# Same concept as above, but applied to a different model (Employees)
class EmoloyeeSerializer(serializers.ModelSerializer):  # typo in class name: should be EmployeeSerializer
    class Meta:
        model = Employees  # Specify the model to serialize
        fields = "__all__"  # Include every field from the Employees model

