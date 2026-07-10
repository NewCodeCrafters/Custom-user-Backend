from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_picture",
            "password",
            "confirm_password",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        # Use your custom manager so the password gets hashed
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        email = attrs.get("email")
        password = attrs.get("password")

        # If your USERNAME_FIELD is email, this works
        user = authenticate(
            username=email,
            password=password,
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        attrs["user"] = user

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
            "profile_picture",
            "is_verified",
            "date_joined",
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
                "Old password is incorrect."
            )

        return value