from django.db import models

# Create your models here.
# ORM (obj relation mapping)
class Genre(models.model):
    name = models.CharField(max_length = 255)

class Movie(models.model):
    title = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.IntegerField()
    image = models.CharField(max_length = 500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
