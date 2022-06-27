from django.http import JsonResponse
from django.shortcuts import render

from property_app.models import Property

# Create your views here.

def property_list(request):
    properties = Property.objects.all()
    data = {
        'properties': list(properties.values())
    }
    
    return JsonResponse(data)


def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    data = {
        'address': property.address,
        'country': property.country,
        'images': property.images,
        'active': property.active,
        'description': property.description
    }
    return JsonResponse(data)