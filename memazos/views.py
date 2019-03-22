from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def definiciones(request):
    return render(request, 'patrones_1.html', {})

def basicos(request):
    return render(request, 'patrones_2.html', {})
