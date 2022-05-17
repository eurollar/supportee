from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=32,
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CreateUserSerializer(UserSerializer):
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        style={'input_type': 'password'}  # Hide password in field
    )

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )

        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(min_length=8, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(min_length=8, required=True, style={'input_type': 'password'})
