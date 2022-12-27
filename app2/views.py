from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return HttpResponse('<h1>seventeen</h1>')

def hello(request):
    return HttpResponse('<h2>straykids</h1>')

