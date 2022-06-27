from property_app.api.serializers import PropertySerializer
from property_app.models import Property
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class PropertyListAPIView(APIView):
    
    def get(self, request):
        properties = Property.objects.all()
        serializer =PropertySerializer(properties, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer =PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        
class PropertyDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)   
        
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def property_list(request):
#     if request.method == 'GET':
#         try:
#             properties = Property.objects.all()
#             serializer =PropertySerializer(properties, many=True)
#             return Response(serializer.data)
#         except Property.DoesNotExist:
#             return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'POST':
#         serializer =PropertySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def property_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             property = Property.objects.get(pk=pk)
#             serializer = PropertySerializer(property)
#             return Response(serializer.data)
#         except Property.DoesNotExist:
#             return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'PUT':
#         property = Property.objects.get(pk=pk)
#         serializer =PropertySerializer(property, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE': 
#         try:
#             property = Property.objects.get(pk=pk)  
#             property.delete()
#         except Property.DoesNotExist:
#             return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
                
#         return Response(status=status.HTTP_204_NO_CONTENT)