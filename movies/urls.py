from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('home_movie/', views.home_movie, name="home_movie"),
    re_path("movie/", views.MovieApiView.as_view()),
    path("action/", views.action, name="action"),
    path("drama/", views.drama, name="drama"),
    path("experimental/", views.experimental, name="experimental"),
    path("horror/", views.horror, name="horror"),
    path("romance/", views.romance, name="romance"),
    path("scifi/", views.scifi, name="scifi"),
    path("series/", views.series, name="series"),
    path("war/", views.war, name="war"),
]