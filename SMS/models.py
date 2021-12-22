# from SMS.forms import UserInfoModelForm
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.urls import reverse
# from .models import UserInfo
from django.contrib.auth.models import User
from Movie.models import Movie
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
import string
import random


def generateUniqueCode():
    length = 12


    while True:
        userID = ''.join(random.choices(string.ascii_letters, k=length))
        if UserInfo.objects.filter(userID=userID).count() == 0:
            break

    return userID


def generateTicketCode():
    while True:
        code = random.randint(1000000000, 9999999999)
        if Ticket.objects.filter(code=code).count() == 0:
            break
    return code



class UserInfo(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    userID      = models.CharField(max_length=18, default=generateUniqueCode, unique=True)
    name        = models.CharField(max_length=100)
    lastName    = models.CharField(max_length=100) 
    age         = models.PositiveIntegerField() 
    gender      = models.CharField(max_length=6)  
    telnum      = models.CharField(max_length=12, unique=True)
    # balance     = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)
    createdAt = models.DateTimeField(auto_now_add=True) 


    def get_absolute_url(self):
        return reverse("profile", kwargs={"uid": self.userID})

    def __str__(self):
        return self.name+' '+self.lastName
    


class Balance(models.Model):
    user        = models.OneToOneField(User, on_delete=DO_NOTHING)
    balance     = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000)


class Ticket(models.Model):
    TEN = 10.00
    TWENTY = 20.00
    FIFTY = 50.00
    VALUE_CHOICES = [
        (TEN, 10.00),
        (TWENTY, 20.00),
        (FIFTY, 50.00),
    ]
    
     
        
 
    code          = models.CharField(max_length=18, default=generateTicketCode, unique=True)
    value         = models.DecimalField(choices=VALUE_CHOICES, default=TEN,decimal_places=2, max_digits=10000)
    used          = models.BooleanField(default=False)
    boughtBy      = models.ForeignKey(User, on_delete=DO_NOTHING, null=True, blank=True)



class Owns(models.Model):
    movie       = models.ForeignKey(Movie, on_delete=DO_NOTHING)
    user        = models.ForeignKey(User, on_delete=DO_NOTHING)
    boughtAt   = models.DateTimeField(auto_now_add=True) 
    



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserInfo.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     # instance.profile.save()
#     instance.userInfo.save()