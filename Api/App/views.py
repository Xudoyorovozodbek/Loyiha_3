from django.shortcuts import render
from rest_framework import generics
from .serializer import FoydalanuvchiSerializer
from .models import Foydalanuvchi, Kitob
from rest_framework import permissions
from .permissions import CheckUser


class Mix(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAuthenticated]
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()

class Mixes(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAuthenticated]
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()


class Test(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated,permissions.IsAuthenticated]
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()






















class FoydalanuvchiListAPIView(generics.ListAPIView):
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()


class FoydalanuvchiCreateAPIView(generics.CreateAPIView):
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()


class FoydalanuvchiUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()


class FoydalanuvchiDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [CheckUser]
    serializer_class = FoydalanuvchiSerializer
    queryset = Foydalanuvchi.objects.all()