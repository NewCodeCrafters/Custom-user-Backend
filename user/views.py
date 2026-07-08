from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import SignupSerializer, LoginSerializer, UserSerializer, UpdateProfileSerializers, ChangePasswordSerializer

class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": "successful",
                    "user" : UserSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)



                },
                status=status.HTTP_201_CREATED,

            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

