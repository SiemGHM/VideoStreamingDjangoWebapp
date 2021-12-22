from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from SMS.models import Owns, Balance, Ticket
from django.contrib.auth.models import User

# from .forms import UserForm
from .models import Movie

# Create your views here.

@login_required(login_url="/login")
def movie_watch_view(request, mid):
    # user = User.objects.get(userID=uid)
    movie = get_object_or_404(Movie, movieID=mid)
    m = len(Owns.objects.filter(user = request.user, movie = movie ))
    print(m)
    if m>0:
        # movie = get_object_or_404(Movie, movieID=mid)
    
        context = {
            'obj' : movie
        }
        return render(request, "movies/watchmovie.html", context)
    else: 

        return purchase(request, mid)




@login_required(login_url="/login")
def purchase(request, mid):
    if request.method == "POST":
        login_data = request.POST.dict()
        user = login_data.get("user")
        movie = login_data.get("movie")
        movie = get_object_or_404(Movie, movieID=mid)
        user = get_object_or_404(User, username = user)
        price = movie.price
        balance = user.balance.balance
        if balance > price:
            balance = Balance.objects.get(user=user)
            balance.balance -=price
            balance.save()
            Owns.objects.create(user = user, movie = movie)
            return movie_watch_view(request, mid)
        else:
            context = {
                'error': "You need more money cuh"
            }
            return render(request, "error/error.html", context)



    movie = get_object_or_404(Movie, movieID=mid)
    context = {
            'obj' : movie
        }
    return render(request, "movies/buymovie.html", context)


