from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>this is my home</h1>')

def second(request):
    return HttpResponse('<h2>this is my favourite place</h1>')
