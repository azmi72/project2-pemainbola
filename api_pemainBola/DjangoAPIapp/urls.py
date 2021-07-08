from django.urls import path
from django.urls import path
from .views import ListPemainBola, DetailPemainBola, ListKlub, DetailKlub

urlpatterns = [
    path('paraPemainBola', ListPemainBola.as_view(), name='paraPemainBola'),
    path('paraPemainBola/<int:pk>/', DetailPemainBola.as_view(), name='siPemainBola'),

    path('paraKlub', ListKlub.as_view(), name='paraKlub'),
    path('paraKlub', DetailKlub.as_view(), name='siKlub'),
]