from django.urls import path
from .views import renderTemplate, renderEmployee

urlpatterns = [
    path('firstTemplate/', renderTemplate),
    path('employee/', renderEmployee)
]