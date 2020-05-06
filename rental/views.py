from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# MVC python manage.py runserver

# defining an endpoint
def index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('Art Lemus')
    
def soon(request):
    return HttpResponse('Page coming soon, stay in touch :) ')