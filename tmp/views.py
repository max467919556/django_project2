from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse ('Привет Джанго')

def catalog(request):
    return HttpResponse ('Каталог')

def temp(request):
    return HttpResponse ('Временный')

