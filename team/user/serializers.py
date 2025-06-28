from rest_framework import serializers
from user.models import CustomUser


class CustomUserSerislizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=['username', 'first_name', 'last_name', 'email', 'phone_number','password']
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserLoginSerislizer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)