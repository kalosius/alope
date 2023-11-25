from django.urls import path
from . import views

urlpatterns = [
    path("weather_status/", views.weather_status, name="weather_status"),
]