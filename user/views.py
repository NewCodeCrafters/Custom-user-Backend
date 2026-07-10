from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import (
    SignupSerializer,
    LoginSerializer,
    UserSerializer,
    UpdateProfileSerializers,
    ChangePasswordSerializer,
)


# Reusable Bearer authentication definition
bearer_auth = [{"Bearer": []}]


class SignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Register a new user",
        operation_description="Creates a new user account and returns JWT access and refresh tokens.",
        request_body=SignupSerializer,
        responses={
            201: UserSerializer,
            400: "Validation Error",
        },
        tags=["Authentication"],
    )
    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Registration successful.",
                    "user": UserSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Login",
        operation_description="Authenticates a user and returns JWT tokens.",
        request_body=LoginSerializer,
        tags=["Authentication"],
    )
    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "Login successful.",
                    "user": UserSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get Profile",
        operation_description="Returns the authenticated user's profile.",
        security=bearer_auth,
        responses={200: UserSerializer},
        tags=["Profile"],
    )
    def get(self, request):

        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update Profile",
        operation_description="Updates the authenticated user's profile.",
        request_body=UpdateProfileSerializers,
        security=bearer_auth,
        responses={200: UserSerializer},
        tags=["Profile"],
    )
    def put(self, request):

        serializer = UpdateProfileSerializers(
            request.user,
            data=request.data,
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Profile updated successfully.",
                    "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_summary="Partial Profile Update",
        operation_description="Updates selected profile fields.",
        request_body=UpdateProfileSerializers,
        security=bearer_auth,
        responses={200: UserSerializer},
        tags=["Profile"],
    )
    def patch(self, request):

        serializer = UpdateProfileSerializers(
            request.user,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Profile updated successfully.",
                    "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Change Password",
        operation_description="Changes the authenticated user's password.",
        request_body=ChangePasswordSerializer,
        security=bearer_auth,
        tags=["Authentication"],
    )
    def put(self, request):

        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request},
        )

        if serializer.is_valid():

            request.user.set_password(
                serializer.validated_data["new_password"]
            )

            request.user.save()

            return Response(
                {
                    "message": "Password changed successfully."
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Logout",
        operation_description="logout by blaclisting refresh token",
        security=bearer_auth,
        tags=["Authentication"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["refresh"],
            properties={
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh Token",
                )
            },
        ),
    )
    def post(self, request):

        try:

            refresh_token = request.data.get("refresh")

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    "message": "Logout successful."
                },
                status=status.HTTP_200_OK,
            )

        except Exception:

            return Response(
                {
                    "error": "Invalid refresh token."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
