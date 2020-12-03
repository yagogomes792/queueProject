from . import views
from django.urls import path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('route', views.route, name='route'),
    path('update', views.update, name='update'),
    path('thanks', views.thanks, name='thanks'),
    path('about', views.about, name='about'),
]