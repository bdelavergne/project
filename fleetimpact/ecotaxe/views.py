# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import render

def ecotaxe(request):
    return render(request, 'ecotaxe/ecotaxe.html')

def reseau(request):
    return render(request, 'ecotaxe/reseau.html')

def optimisation(request):
    return render(request, 'ecotaxe/optimisation_manuelle.html')

def tour_de_france(request):
    return render(request, 'ecotaxe/tour_de_france.html')
