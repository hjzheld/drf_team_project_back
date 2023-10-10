from rest_framework import serializers

from articles.models import Article
from comment.models import Comment
from comment.serializers import CommentSerializer

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image',)

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    def get_user(self, obj):
        return obj.user.nickname
    
    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'image', 'updated_at', 'user', 'comments')
        
        