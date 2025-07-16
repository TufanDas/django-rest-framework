from django.shortcuts import render  # (Optional) Used to render templates — not used in this API view
from django.http import JsonResponse  # Useful for sending JSON responses — also not used here directly
from students.models import Students  # Imports the Students model from the students app
from ..serializers import StudentSerializer  # Imports the serializer to convert model instances to JSON
from rest_framework.response import Response  # A DRF helper to send standard API responses
from rest_framework import status  # Provides HTTP status codes for clarity
from rest_framework.decorators import api_view  # Allows defining function-based views that support REST methods
from rest_framework.views import APIView
from employees.models import Employees
from ..serializers import *
from django.http import Http404
from rest_framework import mixins, generics # Django REST framework mixins and base view


# Generic view
class Employee(generics.ListCreateAPIView):
    # This query retrieves all Employee records from the database
    queryset = Employees.objects.all()

    # Specifies the serializer that converts model instances to JSON (and vice versa)
    serializer_class = EmoloyeeSerializer


# A generic view to handle retrieving, updating, and deleting a single employee
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    # Fetches all Employee records; DRF will pick the one matching the given pk
    queryset = Employees.objects.all()

    # Serializer that defines how Employee data is converted to/from JSON
    serializer_class = EmoloyeeSerializer

    # Tells DRF to look for the employee using the 'pk' (primary key) in the URL
    lookup_field = 'pk'
