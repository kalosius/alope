from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    passwrd1 = models.CharField(max_length=250)
    confirm_password = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + " " + self.last_name





class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + " " + self.lname