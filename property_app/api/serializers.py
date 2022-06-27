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
    
    def update(self, instance, validaded_data):
        instance.address = validaded_data.get('address', instance.address),
        instance.country = validaded_data.get('country', instance.country),
        instance.description = validaded_data.get('description', instance.description),
        instance.images = validaded_data.get('location', instance.images),
        instance.active = validaded_data.get('active', instance.active)
        
        instance.save()
        return instance