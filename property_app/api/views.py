from property_app.api.serializers import PropertySerializer
from property_app.models import Property
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer =PropertySerializer(properties, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer =PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertySerializer(property)
    return Response(serializer.data)