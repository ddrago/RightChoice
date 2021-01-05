from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Context dict test'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'Created by Stuart, Euan, Diego, Zhenkun and Daniyal'}
    return render(request, 'rango/about.html', context=context_dict)

def uni(request):
    context_dict = {'boldmessage': 'Look at all the couses avalible or search for a desired course'}
    return render(request, 'rango/university.html', context=context_dict)

def college(request):
    context_dict = {'boldmessage': 'Look at all the couses avalible or search for a desired course'}
    return render(request, 'rango/college.html', context=context_dict)

def apprenticeship(request):
    context_dict = {'boldmessage': 'Look at all the companies offering apprenticeships'}
    return render(request, 'rango/apprenticeship.html', context=context_dict)
