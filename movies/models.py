from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Serie(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class SciFi(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Drama(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Action(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Exiperimental(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Romance(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class War(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Horror(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)






