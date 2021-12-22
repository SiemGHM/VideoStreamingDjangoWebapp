from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse

# Create your models here.
import string
import random

def generateUniqueCode():
    length = 18


    while True:
        musicID = ''.join(random.choices(string.ascii_letters, k=length))
        if Music.objects.filter(musicID=musicID).count() == 0:
            break

    return musicID


class Music(models.Model):
    musicID      = models.CharField(max_length=20, default=generateUniqueCode, unique=True)
    artist       = models.ForeignKey(Artist, on_delete=DO_NOTHING)
    title        = models.CharField(max_length=100) 
    minAge       = models.PositiveIntegerField() 
    song        = models.FileField(upload_to='songs', default=None)
    thumbnail     = models.FileField(upload_to='thumbnail/',  null=True)
    price        = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)
    createdAt    = models.DateTimeField(auto_now_add=True) 
    streams      = models.PositiveBigIntegerField()

    def __str__(self):
        return "{} {}".format(self.title, self.artist)


    def get_absolute_url(self):
        return reverse("music-main", kwargs={"mid": self.musicID})




def generateUniqueCodeArtist():
    length = 17


    while True:
        artistID = ''.join(random.choices(string.ascii_letters, k=length))
        if Artist.objects.filter(artistID=artistID).count() == 0:
            break

    return artistID


class Artist(models.Model):
    artistID      = models.CharField(max_length=20, default=generateUniqueCode, unique=True)
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
    


    





