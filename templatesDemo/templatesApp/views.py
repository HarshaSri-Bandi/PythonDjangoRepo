from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict ={"name" : "Harsha"}
    return render(request,'templatesApp/firstTemplate.html', myDict)

def renderEmployee(request):
    myDict = {"id" : 123,"name":"Harsha", "sal" : 100000}
    return render(request, 'templatesApp/employeeTemplate.html', myDict)
