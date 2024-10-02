from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index3(request):
    return HttpResponse ('Привет Джанго3')

def catalog3(request):
    return HttpResponse ('Каталог2')

def temp3(request):
    return HttpResponse ('Временный3')