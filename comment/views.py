from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Comment
from user.models import User
from articles.models import Article

from .serializers import CommentSerializer


class CommentView(APIView):
    def post(self, request, article_id):
        """ 특정 게시글에 댓글 작성"""
        article = Article.objects.get(pk=article_id)

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(article_id=article)
        return Response(serializer.data)
    
    def put(self, request, article_id, pk):
        """ 특정 댓글 수정 """
        try:
            comment = Comment.objects.get(pk=pk, user_id=request.user.pk)
        except ObjectDoesNotExist:
            return Response({"message":"수정할 수 없습니다."})

        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, article_id, pk):
        """ 특정 댓글 삭제 """
        try:
            comment = Comment.objects.get(pk=pk, user_id=request.user.pk)
        except ObjectDoesNotExist:
            return Response({"message":"삭제할 수 없습니다."})
        comment.delete()

        return Response({"message":"삭제되었습니다."})
