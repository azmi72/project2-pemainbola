from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import PemainBola, Klub, Favorite
from .serializers import PemainBolaSerializer, KlubSerializer, RegistrationSerializer, UserSerializer, FavoriteSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User Created Succesfully",

                "User": serializer.data}, status.HTTP_201_CREATED
                )
            
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListPemainBola(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PemainBola.objects.all()
    serializer_class = PemainBolaSerializer

class DetailPemainBola(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PemainBola.objects.all()
    serializer_class = PemainBolaSerializer

class ListKlub(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class DetailKlub(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer

class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListFavorite(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class DetailFavorite(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


