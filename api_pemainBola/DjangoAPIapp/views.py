from django.shortcuts import render
from rest_framework import generics
from .models import PemainBola, Klub
from .serializers import PemainBolaSerializer, KlubSerializer

class ListPemainBola(generics.ListCreateAPIView):
    queryset = PemainBola.objects.all()
    serializer_class = PemainBolaSerializer

class DetailPemainBola(generics.RetrieveUpdateDestroyAPIView):
    queryset = PemainBola.objects.all()
    serializer_class = PemainBolaSerializer

class ListKlub(generics.ListCreateAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class DetailKlub(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer
