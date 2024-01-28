from django.shortcuts import render
from rest_framework.response import Response
from .models import Parts, Categories, Location
from .serializers import PartsSerializer, CategoriesSerializer, LocationSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
#1 option, much more scalable and complex
class PartsRW(generics.ListCreateAPIView):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category', 'price', 'location']


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


#alternative endpoint for filters
# class PartsFilter(generics.ListAPIView):
#     queryset = Parts.objects.all()
#     serializer_class = PartsSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name', 'category', 'price', 'location']


#2 much more straight forward option

# class PartsG(generics.ListAPIView):
#     serializer_class = PartsSerializer
#     queryset = Parts.objects.all()


# class PartsCR(generics.ListCreateAPIView):
#     serializer_class = PartsSerializer
#     queryset = Parts.objects.all()


# class PartsUD(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PartsSerializer
#     queryset = Parts.objects.all()


# class LocationG(generics.ListAPIView):
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()


# class LocationCR(generics.ListCreateAPIView):
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()


# class LocationUD(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = LocationSerializer
#     queryset = Location.objects.all()


# class CategoryG(generics.ListAPIView):
#     serializer_class = CategoriesSerializer
#     queryset = Categories.objects.all()


# class CategoryCR(generics.ListCreateAPIView):
#     serializer_class = CategoriesSerializer
#     queryset = Categories.objects.all()


# class CategoryUD(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CategoriesSerializer
#     queryset = Categories.objects.all()
