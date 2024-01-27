from django.shortcuts import render
from rest_framework.response import Response
from .models import Parts, Categories, Location
from .serializers import PartsSerializer, CategoriesSerializer, LocationSerializer
from rest_framework import generics
# Create your views here.

class PartsRW(generics.ListCreateAPIView):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()


class PartRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()


class LocationRW(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class CategoryRW(generics.ListCreateAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()