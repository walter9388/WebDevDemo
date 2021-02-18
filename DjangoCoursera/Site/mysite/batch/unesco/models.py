from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
         return self.name

class Iso(models.Model):
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048, null=True)
    justification = models.CharField(max_length=2048, null=True)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    iso = models.ForeignKey(Iso, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.name
