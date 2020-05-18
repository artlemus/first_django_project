from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse, Http404
=======
from django.http import HttpResponse
>>>>>>> 1b0238e1506683917da9bbff352f0e96276bd91b
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
<<<<<<< HEAD

def details(request, movie_id):
    try:
        the_movie = Movie.objects.get(id=movie_id)
        return render(request, 'details.html', {'movie': the_movie })
    except:
        raise Http404()
        # return render(request, 'NotFound.html')


def catalog(request):
    return render(request, 'catalog.html')
=======
>>>>>>> 1b0238e1506683917da9bbff352f0e96276bd91b

def about(request):
    return HttpResponse('Art Lemus')
    
def soon(request):
<<<<<<< HEAD
    return render(request,'comingSoon.html')


=======
    return render(request,'comingSoon.html')
>>>>>>> 1b0238e1506683917da9bbff352f0e96276bd91b
