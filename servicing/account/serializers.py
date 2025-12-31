from django.contrib.auth.models import User

from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"]
        )
        return user
    

class UserAuthorizationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        try:
            user = User.objects.get(username=data["username"])
        except:
            raise serializers.ValidationError("Пользователь не найден")
        
        if not user.check_password(data["password"]):
            raise serializers.ValidationError("Неверный логин и пароль")
        
        data['user'] = user
        return data