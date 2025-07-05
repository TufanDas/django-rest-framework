from django.urls import path
from . import views

# Define URL patterns for this app
urlpatterns = [
    path('', views.students)
]