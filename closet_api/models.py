from django.db import models

# Create your models here.
class Clothing(models.Model):
    type = models.CharField(max_length=32, default="Blank", editable=True)
    attire = models.CharField(max_length=32, default="Blank", editable=True)
    description = models.CharField(max_length=32, default="Blank", editable=True)
    color = models.CharField(max_length=32, default="Blank", editable=True)
    color_type = models.CharField(max_length=32, default="Blank", editable=True)
