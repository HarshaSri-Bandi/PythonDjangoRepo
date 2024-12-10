from django.urls import path
from .views import employeeData

urlpatterns = [
    path('', employeeData),
]