from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('home_movie/', views.home_movie, name="home_movie"),
    re_path("movie/", views.MovieApiView.as_view()),
]