from django.urls import path  # Imports the path function to define URL patterns
from . import views           # Imports views from the current app directory
from api.view import mixin_views 

# URL configuration for the app
urlpatterns = [
    # Maps the URL 'students/' to the students_view function inside views.py
    path('students/', views.students_view),
    path('students/<int:pk>/', views.studentDetailView),

    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('mixins/employees/', mixin_views.Employeess.as_view()),
    path('mixins/employees/<int:pk>/', mixin_views.EmployeeDetail.as_view()),

    path('generics/employees/', )
]
