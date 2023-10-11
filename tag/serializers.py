from rest_framework import serializers
from tag.models import Tag
from articles.models import Article


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class TagCalSerializer(serializers.ModelSerializer):
    tag_articles = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = "__all__"

    def get_tag_articles(self, tag):
        """ 목표태그별 아티클 갯수(달성률) """
        articles = Article.objects.filter(tag_id=tag.id)
        tag_articles = len(articles)
        return tag_articles