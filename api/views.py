from django.shortcuts import render
from rest_framework.response import Response
from .models import Parts, Categories, Location
from .serializers import PartsSerializer, CategoriesSerializer
from rest_framework.decorators import api_view
from rest_framework import serializers, status, generics
# Create your views here.


# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_parts': '/',
#         'all_categories': '/categories',
#         'Search by Category': '/?category=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/part/pk/delete',
#     }

#     return Response(api_urls)


# @api_view(['GET'])
# def view_parts(request):
     
     
#     # checking for the parameters from the URL
#     if request.query_params:
#         parts = Parts.objects.filter(**request.query_params.dict())
#     else:
#         parts = Parts.objects.all()
 
#     # if there is something in items else raise error
#     if parts:
#         serializer = PartsSerializer(parts, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['POST'])
# def add_parts(request):
#     part = PartsSerializer(data=request.data)

#     if Parts.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This part already existy into warehouse')
    
#     if part.is_valid():
#         part.save()
#         return Response(part.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

class PartsList(generics.ListCreateAPIView):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()


class PartDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartsSerializer
    queryset = Parts.objects.all()
