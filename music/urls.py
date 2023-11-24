from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('songs/', views.songs, name="songs"),
    re_path("song/", views.SongApiView.as_view())
]