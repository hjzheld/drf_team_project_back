from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, UserProfileSerializer
from .models import User

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


# 본인 프로필, 글, 댓글 조회
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        if request.user.id == user_id:
            user = User.objects.filter(id=user_id)
            serializer = UserProfileSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)
