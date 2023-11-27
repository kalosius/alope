from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    movie_name =  models.CharField(max_length =50, null = True, blank = True)
    description = models.CharField(max_length =50, null = True, blank = True)
    




