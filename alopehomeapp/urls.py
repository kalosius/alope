from django.urls import path
from . import views

urlpatterns = [
    path("", views.alope_home, name="alope_home"),
    path("join/", views.join, name="join"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),

]