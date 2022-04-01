from django.db import models

# Create your models here.
class Clothing(models.Model):
    type = models.CharField(max_length=32, default="Top, Bottom, Shoes", editable=True)
    attire = models.CharField(max_length=32, default="Sport, Casual, Business", editable=True)
    description = models.CharField(max_length=32, default="Please Enter a Brief Description", editable=True)
    color = models.CharField(max_length=32, default="Enter Color Here", editable=True)
    color_type = models.CharField(max_length=32, default="Enter color based on color type. See Attached Image", editable=True)
