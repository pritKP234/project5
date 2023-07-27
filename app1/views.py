from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def func1(request):
    return HttpResponse('<marquee><h2>This is function 1 in app 1</marquee></h2>')

def func2(request):
    return HttpResponse('<marquee><h1>This is fuction 2 in app 1</marquee></h1>')