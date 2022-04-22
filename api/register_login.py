from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from .models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


#for the  user register 
class UserRegister(viewsets.ViewSet):
    
    def create(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_response = {"status": status.HTTP_201_CREATED,
                             "header": "application/json", "message": "sucessfully Register..."}
            return Response(json_response)
        json_response = {"status":status.HTTP_403_FORBIDDEN,
                          "response": serializer.errors, "message": "Register not sucess..."}
        return Response(json_response)


# user login functionality 
class UserLogin(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        
        email = request.data.get('email')
        password = request.data.get('password')
        
        if email is None:
            json_response = {"message": "email required",
                             "status": status.HTTP_400_BAD_REQUEST}
            return Response(json_response)
        if password is None:
            json_response = {"message": "Password required",
                             "status": status.HTTP_400_BAD_REQUEST}

        user_vo = User.objects.filter(email=email)
        if len(user_vo) <= 0:
            json_response = {"message": "Please enter valid email",
                             "status": status.HTTP_400_BAD_REQUEST}
            return Response(json_response)

        username = user_vo[0].username
        user = authenticate(username=username, password=password)
        if not user:
            json_response = {"message": "Invalid email or password.",
                             "status": status.HTTP_400_BAD_REQUEST}
            return Response(json_response)
        
        refresh =  RefreshToken.for_user(user)
        json_response = {"access": str(refresh.access_token), "refresh": str(
            refresh), "status": status.HTTP_200_OK}
        
        return Response(json_response)
