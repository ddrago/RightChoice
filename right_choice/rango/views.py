from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Context dict test'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'Created by Stuart, Euan, Diego, Zhenkun and Daniyal'}
    return render(request, 'rango/about.html', context=context_dict)
