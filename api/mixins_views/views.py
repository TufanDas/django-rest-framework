# from django.shortcuts import render  # (Optional) Used to render templates — not used in this API view
# from django.http import JsonResponse  # Useful for sending JSON responses — also not used here directly
# from students.models import Students  # Imports the Students model from the students app
# from ..serializers import StudentSerializer  # Imports the serializer to convert model instances to JSON
# from rest_framework.response import Response  # A DRF helper to send standard API responses
# from rest_framework import status  # Provides HTTP status codes for clarity
# from rest_framework.decorators import api_view  # Allows defining function-based views that support REST methods
# from rest_framework.views import APIView
# from employees.models import Employees
# from ..serializers import *
# from django.http import Http404




# @api_view(['GET','POST'])  # Decorator that allows only GET requests to this view
# def students_view(request):
#     if request.method == "GET":
#         # Retrieves all student records from the database
#         students = Students.objects.all()

#         # Serializes the queryset to JSON (many=True because it's a list)
#         serializer = StudentSerializer(students, many=True)

#         # Returns serialized data with HTTP 200 OK status
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == "POST":
#         # Create a serializer instance with the data sent by the client
#         serializer = StudentSerializer(data=request.data)
        
#         # Check if the incoming data is valid
#         if serializer.is_valid():
#             # If valid, save the new student to the database
#             serializer.save()
            
#             # Return the saved student data with a "201 Created" status
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         # If validation fails, print errors in the console for debugging
#         print(serializer.errors)
        
#         # Return validation errors to the client with a "400 Bad Request" status
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def studentDetailView(request, pk):
#     try:
#         # Try to fetch the student with the given primary key (pk)
#         student = Students.objects.get(pk=pk)
#     except Students.DoesNotExist:
#         # If student not found, log it and return 404 Not Found
#         print("Student with given ID does not exist.")
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         # Serialize the student object into JSON-friendly format
#         serializer = StudentSerializer(student)

#         # Return the serialized data with a 200 OK response
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         # Update the student instance with the new data from the request
#         serializer = StudentSerializer(student, data=request.data)
        
#         # Check if the updated data is valid
#         if serializer.is_valid():
#             # Save the updated student object to the database
#             serializer.save()
            
#             # Return the updated student data with a 200 OK response
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             # If validation fails, return error messages with a 400 Bad Request
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#          # Delete the student record from the database
#         student.delete()

#          # Return 204 No Content to indicate successful deletion
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Your Employee API View class
# class Employee(APIView):

#     # Handle GET requests - retrieve and return all employee records
#     def get(self, request):
#         # Fetch all employee objects from the database
#         employees_data = Employees.objects.all()

#         # Serialize the queryset into Python native datatypes (usually a list of dictionaries)
#         serializer = EmoloyeeSerializer(employees_data, many=True)  # 'many=True' because we're serializing multiple objects

#         # Return serialized data with HTTP 200 OK status
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # Handle POST requests - add a new employee record to the database
#     def post(self, request):
#         # Extract data sent in the request body (usually JSON)
#         employees_data = request.data

#         # Initialize the serializer with the incoming data
#         serializer = EmoloyeeSerializer(data=employees_data)

#         # Check if the data is valid (e.g., passes model constraints)
#         if serializer.is_valid():
#             # Save the new employee record to the database
#             serializer.save()

#             # Return the serialized data and a 201 CREATED response
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         # If validation fails, return error details with a 400 BAD REQUEST
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # This class handles operations for a single employee based on their primary key (pk)
# class EmployeeDetail(APIView):

#     # Helper method to fetch a specific employee object from the database
#     def get_object(self, pk):
#         try:
#             # Try to retrieve the employee with the given primary key
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             # If the employee is not found, raise a 404 error
#             raise Http404

#     # Handle GET requests to retrieve details of a single employee
#     def get(self, request, pk):
#         # Get the employee object using the helper method
#         employee_object = self.get_object(pk)

#         # Serialize the employee object into a JSON-friendly format
#         serializer = EmoloyeeSerializer(employee_object)

#         # Return the serialized data with a 200 OK status
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # Handle PUT requests to update an existing employee's details
#     def put(self, request, pk):
#         # Step 1: Retrieve the existing employee object from the database
#         employee_object = self.get_object(pk)

#         # Step 2: Pass the new data to the serializer for validation and updating
#         serializer = EmoloyeeSerializer(employee_object, data=request.data)

#         # Step 3: If the data is valid, save the updated object
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         # Step 4: If validation fails, return a 400 response with the errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Handle DELETE requests to remove an employee from the system
#     def delete(self, request, pk):
#         # Step 1: Fetch the employee object to be deleted
#         employee = self.get_object(pk)

#         # Step 2: Delete the employee record from the database
#         employee.delete()

#         # Step 3: Return a 204 No Content status to indicate successful deletion
#         return Response(status=status.HTTP_204_NO_CONTENT)



