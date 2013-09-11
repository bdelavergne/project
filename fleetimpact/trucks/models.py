from django.db import models

# Create your models here.

class Trucks(models.Model):
    type = models.CharField(max_length=30)
