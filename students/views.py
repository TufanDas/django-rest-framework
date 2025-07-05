from django.shortcuts import render  # Used to render HTML templates with context data
from django.http import HttpResponse  # Used to return simple HTTP responses (text or HTML)


# Create your views here.
# This function handles incoming requests to the 'students' route.
# Right now, it's just sending back a simple HTML message.
def students(request):
    return HttpResponse("<h1>Hello students</h1>")
