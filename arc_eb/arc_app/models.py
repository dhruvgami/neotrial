from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    pid = models.CharField(max_length=15)


