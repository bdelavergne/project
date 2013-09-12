from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def thanks(request):
    return render(request, 'thanks.html')
