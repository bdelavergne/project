from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def thanks(request):
    return render(request, 'thanks.html')


def signin(request):
    return render(request, 'signin.html')


def test_maps(request):
    return render(request, 'test_maps.html')

def test_maps2(request):
    return render(request, 'test_maps2.html')

def test_maps3(request):
    return render(request, 'test_maps3.html')

def test_maps4(request):
    return render(request, 'test_maps4.html')

def homepage2(request):
    return render(request, 'dashboard2.html')
