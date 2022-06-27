from rest_framework import serializers

from property_app.models import Property

class PropertySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    address = serializers.CharField()
    country = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    images = serializers.CharField()
    
    def create(self,validated_data):
        return Property.objects.create(**validated_data)