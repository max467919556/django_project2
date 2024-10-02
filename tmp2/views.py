from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index2(request):
    return HttpResponse ('Привет Джанго2')

def catalog2(request):
    return HttpResponse ('Каталог2')

def temp2(request):
    return HttpResponse ('Временный2')