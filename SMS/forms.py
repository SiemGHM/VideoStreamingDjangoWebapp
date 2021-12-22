from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfo
 
# from .models import User

import string
import random

from django.forms.forms import Form


def generateUniqueCode():
    length = 12


    while True:
        userID = ''.join(random.choices(string.ascii_letters, k=length))
        # if User.objects.filter(userID=userID).count() == 0:
        #     break

    return userID




class UserInfoModelForm(ModelForm):
    pass
    class Meta:
        model = UserInfo
        fields = ['telnum', 'name', 'lastName', 'gender', 'age']

    # username = forms.CharField(label="username", max_length=200)
    # name  = forms.CharField(label="Name", max_length=200)
    # lastName  = forms.CharField(label="Last Name", max_length=200)
    # telnum = forms.CharField(label="Telephone number", max_length=30)
    # gender = forms.CheckboxInput({"Male": "Male", "Female":"Female"})
    # age = forms.CharField(label="Age")
    # password = forms.CharField(widget=forms.PasswordInput)
    

    # username = forms.CharField(label="username", max_length=200)

     

    # userID      = forms.CharField(max_length=18, default=generateUniqueCode(), unique=True)
    # name        = forms.CharField(max_length=100)
    # lastName    = forms.CharField(max_length=100) 
    # age         = forms.IntegerField() 
    # gender      = forms.CharField(max_length=6)  
    # telnum      = forms.CharField(max_length=12)    
    # balance     = forms.DecimalField(decimal_places=2, max_digits=10000)
    # createdAt   = forms.DateTimeField()

    # title = forms.CharField(label="tell my man", widget=forms.TextInput(attrs={"placeholder":"shut up"}))
    

    def clean_telnum(self, *args, **kwargs):
        telnum = self.cleaned_data.get("telnum")
        if "07" not in telnum:
            raise forms.ValidationError("Telephone Number must start with 07")
        if len(telnum) != 8:
            raise forms.ValidationError("The length of the Telephone number given is incorrect!")
        else:
            return telnum



    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        # print(password, password2)

        if len(password) < 6:
            raise forms.ValidationError("Password Too Short!")

        elif password2 != password:
            raise forms.ValidationError("Passwords are not matching!")

        else:
            return password

    # def clead_password2(self, *args, **kwargs):
    #     pass2 = self.cleaned_data.get("password2")
    #     passori = self.cleaned_data.get("password")

    #     if pass2 != passori:
    #         raise forms.ValidationError("Passwords are not matching")
        
    #     else:
    #         return pass2
