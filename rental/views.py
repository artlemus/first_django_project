from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.
# MVC python manage.py runserver

# python manage.py makemigrations
# python manage.py migrate

# Admin 
# python manage.py createsuperuser


# defining an endpoint
def index(request):
    all_movies = Movie.objects.all() #read the  movie table to list
    return render(request,'index.html',{'title':'Movies Catalog', 'movies': all_movies })

def details(request, movie_id):
    try:
        the_movie = Movie.objects.get(id=movie_id)
        return render(request, 'details.html', {'movie': the_movie })
    except:
        raise Http404()
        # return render(request, 'NotFound.html')


def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, 'about.html')
    
def soon(request):
    return render(request,'comingSoon.html')

def order(request):
    return render(request,'order.html')


