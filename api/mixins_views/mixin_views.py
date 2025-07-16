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



# A generic API view to handle listing and creating employee records
class Employeess(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # Set the queryset to retrieve all Employee records
    queryset = Employees.objects.all()
    
    # Use the EmoloyeeSerializer to convert model instances to JSON and vice versa
    serializer_class = EmoloyeeSerializer

    # Handle GET requests to list all employees
    def get(self, request):
        return self.list(request)

    # Handle POST requests to create a new employee record
    def post(self, request):
        return self.create(request)

    
# A view for handling single employee details using generic mixins
class EmployeeDetail(
    mixins.RetrieveModelMixin,    # for GET (retrieve)
    mixins.UpdateModelMixin,      # for PUT (update)
    mixins.DestroyModelMixin,     # for DELETE (remove)
    generics.GenericAPIView ):    # base view for mixins


    # Query all employee records from the database
    queryset = Employees.objects.all()

    # Define which serializer to use for this view
    serializer_class = EmoloyeeSerializer

    # Handle GET request for a specific employee (by primary key)
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # Handle PUT request to update a specific employee
    def put(self, request, pk):
        return self.update(request, pk)

    # Handle DELETE request to remove a specific employee
    def delete(self, request, pk):
        return self.destroy(request, pk)
