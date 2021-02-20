from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import authenticate

from rest_framework_jwt.settings import api_settings

from .serializers import CustomUserSerializer
from .models import CustomUser


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        serializer = CustomUserSerializer(request.data)

        if serializer.is_valid():
            user = authenticate(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password']
                )
            
            if user is not None:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                return Response({'msg': 'Login Success', 'token': token, 'user': user}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'Credentials are not valid!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = CustomUserSerializer(request.data)

        if serializer.is_valid():
            user = CustomUser(
                email=serializer.validated_data['email'], password=serializer.validated_data['password']
            )
            user.save()
            return Response({'msg': 'Register Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Register Fail', 'err': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)