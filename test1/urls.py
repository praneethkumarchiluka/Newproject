# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib import admin  
from . import views

app_name='test1'
urlpatterns = [
    path('admin/',admin.site.urls),  
    path('', views.show,name='show'),
    ]
