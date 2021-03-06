"""FCC_DJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from SMS.views import home_view, user_create_view, user_update_view, user_delete_view, recharge
from Movie.views import movie_watch_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index',home_view, name="home"),
    path('home/',home_view, name="home"),
    path('admin/', admin.site.urls),
    path('register', user_create_view, name='signup'),
    path('recharge', recharge, name='recharge'),
    path('profile/<str:uid>', user_update_view, name='profile'),
    path('profile/<str:uid>/delete', user_delete_view, name='delete'),
    path('movie/<str:mid>', movie_watch_view, name='movie-main'),
    path('', include("django.contrib.auth.urls"))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
