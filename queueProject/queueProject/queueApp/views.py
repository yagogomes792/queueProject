from django.shortcuts import render, redirect
from django import template
from django.template.loader import get_template
from django.views import generic
from django.urls import reverse
from .forms import AddTimeForm
from .models import AddWaitTime

# Create your views here.
def home(request):
    template_name = 'index.html'
    return render(request, template_name )

def route(request):
    template_name = 'route.html'
    return render(request, template_name)

def update(request):
    if request.method == 'POST':
        form = AddTimeForm(request.POST)
        if form.is_valid():
            salvar = form.save(commit=False)
            salvar.save()
            return redirect('thanks')
        else:
            return render(request, 'update.html', {'form':form})
    else:
        form = AddTimeForm()
        return render(request, 'update.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')


def about(request):
    return render(request,'about.html')
