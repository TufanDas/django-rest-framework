from django.shortcuts import render  # (Optional) Used to render templates — not used in this API view
from django.http import JsonResponse  # Useful for sending JSON responses — also not used here directly
from students.models import Students  # Imports the Students model from the students app
from .serializers import StudentSerializer  # Imports the serializer to convert model instances to JSON
from rest_framework.response import Response  # A DRF helper to send standard API responses
from rest_framework import status  # Provides HTTP status codes for clarity
from rest_framework.decorators import api_view  # Allows defining function-based views that support REST methods

@api_view(['GET'])  # Decorator that allows only GET requests to this view
def students_view(request):
    if request.method == "GET":
        # Retrieves all student records from the database
        students = Students.objects.all()

        # Serializes the queryset to JSON (many=True because it's a list)
        serializer = StudentSerializer(students, many=True)

        # Returns serialized data with HTTP 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)