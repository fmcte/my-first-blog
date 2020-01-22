# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:03:29 2020

@author: fmcte
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),       
]