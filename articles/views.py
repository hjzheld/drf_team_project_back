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
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass

    def put(self, request, article_id):
        pass

    def delete(self, request, article_id):
        pass
