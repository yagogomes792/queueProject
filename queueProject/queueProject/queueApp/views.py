from django.shortcuts import render
from django import template
from django.template.loader import get_template
from django.views import generic
from django.urls import reverse

# Create your views here.
def home(request):
    template_name = 'index.html'
    return render(request, template_name )

def route(request):
    template_name = 'route.html'
    return render(request, template_name)

def update(request):
    template_name = 'update.html'
    return render(request, template_name)