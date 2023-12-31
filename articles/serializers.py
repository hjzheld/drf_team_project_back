from rest_framework import serializers

from articles.models import Article
from comment.models import Comment
from comment.serializers import CommentSerializer
from tag.models import Tag
from django.conf import settings

class ArticleSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Article
        fields = '__all__'

    def get_tag(self, obj):
        """ 태그 이름 전달 """
        tag = obj.tag_id
        if not tag:
            tag_name = "#목표따윈없는사람"
        else:
            tag_name = tag.tag_name
        return tag_name
    
    def get_nickname(self, obj):
        return obj.user.nickname
    
    def get_profile(self, obj):
        if obj.user.profile:
            profile_url = settings.MEDIA_URL + str(obj.user.profile)
            return profile_url
        else:
            return 'uploads/profiles/default_profile.png'
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image', 'tag_id')

class ArticleListSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Article
        fields = '__all__'

    def get_tag(self, obj):
        """ 태그 이름 전달 """
        tag = obj.tag_id
        if not tag:
            tag_name = "#목표따윈없는사람"
        else:
            tag_name = tag.tag_name
        return tag_name
    
    def get_nickname(self, obj):
        return obj.user.nickname
    
    def get_profile(self, obj):
        if obj.user.profile:
            profile_url = settings.MEDIA_URL + str(obj.user.profile)
            return profile_url
        else:
            return 'uploads/profiles/default_profile.png'