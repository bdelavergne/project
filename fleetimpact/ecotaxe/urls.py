# URLconf here

from django.conf.urls import patterns, url
from ecotaxe.views import ecotaxe, reseau, optimisation, tour_de_france

urlpatterns = patterns('', 
    url(r'^$', ecotaxe), 
    url(r'^reseau$', reseau),
    url(r'^optimisation', optimisation),
    url(r'^tourdefrance', tour_de_france),
)
