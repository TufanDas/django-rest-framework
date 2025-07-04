from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students


# Create your views here.
def students_view(request):
    student = Students.objects.all()
    student = list(student.values())
    print(student)
    return JsonResponse(student, safe=False)