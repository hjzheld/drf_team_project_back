from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import ArticleListSerializer
from comment.serializers import CommentSerializer


# 프로필 조회
class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    article_set = ArticleListSerializer(many=True)
    comments = CommentSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['email', 'nickname', 'profile', 'mbti', 'blog', "followings", "followers", "article_set", "comments", "like_articles"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    # 회원가입    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'profile', 'mbti', 'blog']  


# 로그인         
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['nickname'] = user.nickname
        return token