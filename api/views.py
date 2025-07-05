from django.shortcuts import render  # (Optional) Used to render templates — not used in this API view
from django.http import JsonResponse  # Useful for sending JSON responses — also not used here directly
from students.models import Students  # Imports the Students model from the students app
from .serializers import StudentSerializer  # Imports the serializer to convert model instances to JSON
from rest_framework.response import Response  # A DRF helper to send standard API responses
from rest_framework import status  # Provides HTTP status codes for clarity
from rest_framework.decorators import api_view  # Allows defining function-based views that support REST methods

@api_view(['GET','POST'])  # Decorator that allows only GET requests to this view
def students_view(request):
    if request.method == "GET":
        # Retrieves all student records from the database
        students = Students.objects.all()

        # Serializes the queryset to JSON (many=True because it's a list)
        serializer = StudentSerializer(students, many=True)

        # Returns serialized data with HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        # Create a serializer instance with the data sent by the client
        serializer = StudentSerializer(data=request.data)
        
        # Check if the incoming data is valid
        if serializer.is_valid():
            # If valid, save the new student to the database
            serializer.save()
            
            # Return the saved student data with a "201 Created" status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If validation fails, print errors in the console for debugging
        print(serializer.errors)
        
        # Return validation errors to the client with a "400 Bad Request" status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def studentDetailView(request, pk):
    try:
        # Try to fetch the student with the given primary key (pk)
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        # If student not found, log it and return 404 Not Found
        print("Student with given ID does not exist.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Serialize the student object into JSON-friendly format
        serializer = StudentSerializer(student)

        # Return the serialized data with a 200 OK response
        return Response(serializer.data, status=status.HTTP_200_OK)