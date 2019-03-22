from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patrones_definiciones', views.definiciones, name='patrones1'),
    path('patrones_basicos', views.basicos, name='patrones2'),
    # path('/elementos_basic', views.elementos, name='elementos'),
]
