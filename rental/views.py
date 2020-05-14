from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
# MVC python manage.py runserver

# defining an endpoint
def index(request):
    all_movies = Movie.objects.all() #read the  movie table to list
    return render(request,'index.html',{'title':'Movies Catalog', 'movies': all_movies })

def about(request):
    return HttpResponse('Art Lemus')
    
def soon(request):
    return render(request,'comingSoon.html')