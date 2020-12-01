from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Context dict test'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the about page! <a href='http://127.0.0.1:8000/'>Back to home</a>")
# Create your views here.
