from django.urls import path
from . import views

urlpatterns = [
    path('', views.alope_home, name="alope_home"),

]