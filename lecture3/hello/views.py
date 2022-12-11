from django.http import HttpResponse
from django.shortcuts import render
name = "Caesar Dave"
# Create your views here.
def index(request):
    return render(request, "hello/index.html",{
    "name": name
    }) 

def brian(request):
    return HttpResponse("Hello, Brian")

def caes(request):
    return HttpResponse("Hello, Caes")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })