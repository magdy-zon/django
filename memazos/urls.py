from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/elementos_basic', views.elementos, name='elementos'),
]
