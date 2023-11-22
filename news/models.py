from django.db import models

# Create your models here.
class Trending(models.Model):
    url = models.URLField(max_length=2850)

class Breaking_news(models.Model):
    headline = models.CharField(max_length=250)

class International_news(models.Model):
    url = models.URLField(max_length=2850)

