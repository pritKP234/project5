from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def func3(request):
    return HttpResponse('<marquee><h1>This is function 3 in app2</h1></marquee>')

def func4(request):
    return HttpResponse('<marquee><h2>This is function 4 in app2</h2></marquee>')