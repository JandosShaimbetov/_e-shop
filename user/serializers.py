from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "check_password",
            "address",
            "phone",
        ]

        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True},
            "address": {"required": True},
            "phone": {"required": True},
        }

    def create(self, validated_data):
        if validated_data["password"] != validated_data["check_password"]:
            raise serializers.ValidationError("invalid password")
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            address=validated_data["address"],
            phone=validated_data["phone"],
        )
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": ("invalid token")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
