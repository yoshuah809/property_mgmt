from django.http import JsonResponse
from django.shortcuts import render

from property_app.models import Property

# Create your views here.

def property_list(self):
    properties = Property.objects.all()
    data = {
        'properties': list(properties.values())
    }
    
    return JsonResponse(data)