from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayQuote(request):
    return HttpResponse("<h1>The best investment we can make is in ourselves</h1>")