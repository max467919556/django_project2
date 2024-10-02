"""
URL configuration for django_project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tmp import views as views_tmp
from tmp2 import views as views_tmp2
from tmp3 import views as views_tmp3

urlpatterns = [
    path('index/', views_tmp.index),
    path('catalog/', views_tmp.catalog),
    path('temp/', views_tmp.temp),
    path('index2/', views_tmp2.index2),
    path('catalog2/', views_tmp2.catalog2),
    path('temp2/', views_tmp2.temp2),
    path('index3/', views_tmp3.index3),
    path('catalog3/', views_tmp3.catalog3),
    path('temp3/', views_tmp3.temp3),
]