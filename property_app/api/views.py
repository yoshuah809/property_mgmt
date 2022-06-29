from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from property_app.api.serializers import CommentSerializer, PropertySerializer, CompanySerializer
from property_app.models import Comment, Property, Company
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins,generics,viewsets
from rest_framework.views import APIView


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        property = Property.objects.get(pk=pk)
        
        user=self.request.user
        comment_queryset = Comment.objects.filter(property =property, user_account=user)
        
        if comment_queryset.exists():
            raise ValidationError("The user already has a comment for this property")
        serializer.save(property=property, user_account=user)
        
    

class CommentList(generics.ListCreateAPIView):
    #queryset = Comment.Objects.all()
    serializer_class = CommentSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(property=pk)
    
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
        

# class CommentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class CommentDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)    

class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        properties = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(properties)
        return Response(serializer.data)
        
    def create(self, request):
        serializer =CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def put(self, request, pk):
        serializer =CompanySerializer(data=request.data)
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        
    def destroy(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)   
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer =CompanySerializer(companies, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer =CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class CompanyDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CompanySerializer(company, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)   
        
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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