from django.urls import path  # Imports the path function to define URL patterns
from . import views           # Imports views from the current app directory
from api.mixins_views import mixin_views 
from api.generic_views import generic_view 

# URL configuration for the app
urlpatterns = [
    # Maps the URL 'students/' to the students_view function inside views.py
    path('students/', views.students_view),
    path('students/<int:pk>/', views.studentDetailView),

    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('mixins/employees/', mixin_views.Employeess.as_view()),
    path('mixins/employees/<int:pk>/', mixin_views.EmployeeDetail.as_view()),

    path('generic/employees/', generic_view.Employee.as_view()),
    path('generic/employees/<int:pk>/', generic_view.EmployeeDetail.as_view()),
    
]
