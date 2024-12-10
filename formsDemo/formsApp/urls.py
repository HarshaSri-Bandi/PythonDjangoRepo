from django.urls import path
from .views import userRegistrationView
urlpatterns = [
    path('', userRegistrationView)
]