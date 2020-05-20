from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='homepage'),
    path('home', views.index, name='homepage'),
    path('about', views.about, name='aboutpage'),
    path('catalog', views.catalog, name='catalog'),
    path('details', views.soon, name='details'),
    path('user/login', views.soon, name='login'),
    path('order', views.order, name='order'),
    path('movie/<int:movie_id>', views.details, name='details'),
]