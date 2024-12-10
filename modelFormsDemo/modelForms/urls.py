from django.urls import path
from .views import index, listProjects, addProject

urlpatterns = [
    path('', index),
    path('ListProjects/', listProjects),
    path('addProjects/', addProject),
]