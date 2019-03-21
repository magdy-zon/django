from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patrones_primero', views.patrones1, name='patrones1'),
    path('patrones_segundo', views.patrones2, name='patrones2'),
    # path('/elementos_basic', views.elementos, name='elementos'),
]
