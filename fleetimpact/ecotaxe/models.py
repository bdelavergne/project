from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join
from fleetimpact.settings import MEDIA_ROOT

class Ecotaxe(models.Model):
    route = models.CharField(max_length=60)
    proprietaire = models.CharField(max_length=60)
    numero_tarification = models.IntegerField()
    sens_circulation = models.CharField(max_length=60)
    descripteur = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=12, decimal_places=10, blank=True, default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=10, blank=True, default=0)
    longeur= models.DecimalField(max_digits=12, decimal_places=10, blank=True, default=0)

    def __unicode__(self):
        return unicode(self.route) + " : ( " + unicode(self.latitude) +", "+unicode(self.longitude)+ " sur " + unicode(self.longeur)
