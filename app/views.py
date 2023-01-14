from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hai(request,name):
    return HttpResponse(f'<h1>welcome to hai page to {name}</h1>')
def hello(request,name):
    return HttpResponse(f'<center><h1>welcome to hello page to {name}</h1></center>')
