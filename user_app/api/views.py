from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer
from user_app import models
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        
        if serializer.is_valid():
            account=serializer.save()
            data['response']='User was successfully registered'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token']= token
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data=serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)    