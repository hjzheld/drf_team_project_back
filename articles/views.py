from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# 회원가입
class ArticleView(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass

    def put(self, request, article_id):
        pass

    def delete(self, request, article_id):
        pass
    
class CommentView(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass

class LikeView(APIView):
    def post(self, request):
        pass
