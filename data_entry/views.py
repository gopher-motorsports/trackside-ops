from django.shortcuts import render
from .models import *

def home(request):
    context = {}
    return render(request, 'data_entry/home.html', context)

def collectData(request):
    context = {}
    return render(request, 'data_entry/collectdata.html', context)

def viewData(request):
    context = {}
    return render(request, 'data_entry/viewdata.html', context)
