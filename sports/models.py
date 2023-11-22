from django.db import models

# Create your models here.
class All_Sport(models.Model):
    game = models.CharField(max_length=250)

class English_Leagues(models.Model):
    game = models.CharField(max_length=250)

class Spanish_Leagues(models.Model):
    game = models.CharField(max_length=250)

class Germany_Leagues(models.Model):
    game = models.CharField(max_length=250 )

class Champions_League(models.Model):
    game = models.CharField(max_length=250 )


