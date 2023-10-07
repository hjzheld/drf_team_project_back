from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleCreateSerializer


class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK )
    
    def post(self, request):
        user = request.user

        Serializer = ArticleSerializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save(author=user)

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK )

    def put(self, request, article_id):
        article = Article.objects.get(author=request.user)

        Serializer = ArticleSerializer(article, data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()

    def delete(self, request, article_id):
        pass
