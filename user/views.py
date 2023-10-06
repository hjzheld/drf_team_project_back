from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

# 회원가입
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer['email'])
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        elif 'nickname' in serializer.errors and 'email' in serializer.errors:
            return Response({"message":"이미 가입되어 있는 이메일, 닉네임입니다"}, status=status.HTTP_409_CONFLICT)
        elif 'email' in serializer.errors :
            return Response({"message":"이미 가입되어 있는 이메일입니다"}, status=status.HTTP_409_CONFLICT)
        elif 'nickname' in serializer.errors :
            return Response({"message":"이미 가입되어 있는 닉네임입니다"}, status=status.HTTP_409_CONFLICT)
    
        else :
            return Response({"message":f"$({serializer.errors})"}, status=status.HTTP_400_BAD_REQUEST)


#로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

