from django.urls import path
from django.urls import path
from .views import ListPemainBola, DetailPemainBola, ListKlub, DetailKlub, ListUser, DetailUser, ListFavorite, DetailFavorite

urlpatterns = [
    path('paraPemainBola', ListPemainBola.as_view(), name='paraPemainBola'),
    path('paraPemainBola/<int:pk>/', DetailPemainBola.as_view(), name='siPemainBola'),

    path('paraKlub', ListKlub.as_view(), name='paraKlub'),
    path('paraKlub/<int:pk>/', DetailKlub.as_view(), name='siKlub'),

    path('paraUser', ListUser.as_view(), name='paraUser'),
    path('paraUser/<int:pk>/', DetailUser.as_view(), name='siUser'),

    path('paraFavorite', ListFavorite.as_view(), name='paraFavorite'),
    path('paraFavorite/<int:pk>/', DetailFavorite.as_view(), name='siFavorite'),
]