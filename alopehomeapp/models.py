from django.db import models

# Create your models here.
class Movie(models.Model):
    last_updated = models.DateTimeField(auto_now=True)