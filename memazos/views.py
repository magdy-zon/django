from django.shortcuts import render

# Create your views here.
def index(request):
    return get_response("Hola amigos")
