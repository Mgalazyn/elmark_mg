from django.shortcuts import render
from rest_framework.response import Response
from .models import Parts, Categories
from .serializers import PartsSerializer, CategoriesSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_parts': '/',
        'all_categories': '/categories',
        'Search by Category': '/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/part/pk/delete',
    }

    return Response(api_urls)

