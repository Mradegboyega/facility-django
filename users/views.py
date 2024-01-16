from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




# Create your views here.

def index(request: HttpRequest):
    return render(request, 'user_home.html')

def greet(request: HttpRequest):
    return render(request, 'greet.html')