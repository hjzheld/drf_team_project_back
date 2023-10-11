from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleListSerializer, ArticleSerializer, ArticleCreateSerializer
from user.models import User


class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'message':'다시 로그인 해주세요.'}, status=status.HTTP_401_UNAUTHORIZED)
   
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message':'등록되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializers = ArticleListSerializer(article)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'message':'수정 되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED) 


    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response({'message':'삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


class LikeView(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response('좋아요 취소', status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response('좋아요 완료', status=status.HTTP_200_OK)
       
