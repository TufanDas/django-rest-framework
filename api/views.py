from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def students_view(request):
    student = {
        'id' : 1,
        'name':"Tufan Das",
        'class' : "Computer science"
    }
    return JsonResponse(student)