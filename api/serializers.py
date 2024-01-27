from rest_framework import serializers
from .models import Categories, Parts, Location

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

    
class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(PartsSerializer, self).to_representation(instance)
        location_instance = instance.location
        
        return {
            **representation,
            'location': str(location_instance) if location_instance else None
        }