from django.db import models

# Create your models here.
class Pop(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class RnB(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Rock(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Gospel(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class HipHop_Rap(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Electronic(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Country(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Jazz(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

class Reggae(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=250)

