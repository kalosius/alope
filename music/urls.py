from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('songs/', views.songs, name="songs"),
    re_path("song/", views.SongApiView.as_view()),
    path('country/', views.country, name='country'),
    path("jazz/", views.jazz, name="jazz"),
    path("hiphop/", views.hiphop, name="hiphop"),
    path("reggae/", views.reggae, name="reggae"),
    path("rock/", views.rock, name="rock"),
    path("gospel/", views.gospel, name="gospel"),
    path("rnb/", views.rnb, name="rnb"),
    path("pop/", views.pop, name="pop"),
    path("electronic/", views.electronic, name="electronic"),
    

]