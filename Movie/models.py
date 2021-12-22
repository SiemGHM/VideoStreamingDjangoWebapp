from django.db import models
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
import string
import random

def generateUniqueCode():
    length = 20


    while True:
        MovieID = ''.join(random.choices(string.ascii_letters, k=length))
        if Movie.objects.filter(movieID=MovieID).count() == 0:
            break

    return MovieID


class Movie(models.Model):
    movieID      = models.CharField(max_length=20, default=generateUniqueCode, unique=True)
    title        = models.CharField(max_length=100) 
    minAge       = models.PositiveIntegerField() 
    # rating       = models.PositiveIntegerField(default=3)
    video        = models.FileField(upload_to='videos/', default=None)
    trailer       = models.FileField(upload_to='trailer/',  null=True)
    thumbnail     = models.FileField(upload_to='thumbnail/',  null=True)

    price        = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)
    createdAt    = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse("movie-main", kwargs={"mid": self.movieID})
    

