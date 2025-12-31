from django.shortcuts import render
from rest_framework.authtoken.models import Token
from account.serializers import UserRegistrationSerializer, UserAuthorizationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def registration(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь создан"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        serializer = UserAuthorizationSerializer(data = request.data)
        if serializer.is_valid():
            # Получаем объект пользователя
            user = serializer.validated_data["user"]

            token, created = Token.objects.get_or_create(user=user)


            return Response({
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Введите логин и пароль"}, status=status.HTTP_200_OK)



