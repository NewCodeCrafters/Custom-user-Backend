from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class SignupSerializer(serializers.Modelserializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm-password = serializers.CharField(write_only=True)

    class Meta:
        models = User
        fields = (
            "id",
            "first_name"
            "last_name",
            "email",
            "phone_number"
            "profile_pic",
            "password",
            "confirm_password",
        )
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "password does not match"}
            )
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        return User.objects.create(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            email=email, password = password
        )
        if not user:
            raise serializers.ValidationError(
                "invalid email or password"
            )
        attrs["user"]= user
        return attrs
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_picture"
            "is_verified"
            "date_joined"

        )

class UpdateProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "profile_picture",
            "phone_number",
        )

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8)

    def validate_old_password(self, value):
        user = self.context["request"].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                "old password is Incorrect"
            )
        return value