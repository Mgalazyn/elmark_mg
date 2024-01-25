from rest_framework import serializers
from .models import Categories, Parts

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'