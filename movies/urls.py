from django.urls import path
from . import views

urlpatterns = [
    path('home_movie/', views.home_movie, name="home_movie")
]