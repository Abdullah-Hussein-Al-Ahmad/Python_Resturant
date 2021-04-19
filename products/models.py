from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.CharField(max_length=2083)
    image_link = models.CharField(max_length=2000000)

class Login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
