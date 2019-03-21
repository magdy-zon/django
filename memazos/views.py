from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def patrones1(request):
    return render(request, 'patrones_1.html', {})

def patrones2(request):
    return render(request, 'patrones_2.html', {})
