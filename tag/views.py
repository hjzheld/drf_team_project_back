from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import get_object_or_404

from .models import Tag
from user.models import User
from articles.models import Article

from .serializers import TagSerializer


class TagView(APIView):
    def post(self, request):
        """ 목표를 직접 생성 """

        # 중복 체크
        tag_names = Tag.objects.filter(tag_name=request.data["tag_name"])
        if tag_names:
            return Response({"message":"이미 존재하는 목표이름 입니다."}, status=status.HTTP_409_CONFLICT)
        
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(pk=request.user.pk)
        user.tag_ids.add(serializer.data['id'])
        return Response({"message":"성공."}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        """ 이미 있는 목표를 설정 """
        user = User.objects.get(pk=request.user.pk)
        if user.tag_ids == pk:
            return Response({"message":"이미 설정된 목표입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                tag = Tag.objects.get(pk=pk)
                user.tag_ids.add(tag)
            except ObjectDoesNotExist:
                return Response({"message":"존재하지 않는 태그입니다."}, status=status.HTTP_400_BAD_REQUEST)


            return Response({"message":"성공."}, status=status.HTTP_200_OK)
    
    def get(self, request):
        """ tag 조회 요청 """
        tags = Tag.objects.all()
        tag_data =[]
        for i in tags:
            tag_data.append({i.id: i.tag_name})

        return Response(tag_data, status=status.HTTP_200_OK)
    

class TagCalView(APIView):
    def get(self, request, nickname):
        """ 유저의 목표태그와 달성률 요청 """
        user = User.objects.get(nickname=nickname)
        tags = user.tag_ids.all()
        tag_data =[]
        for i in tags:
            tag_articles = Article.objects.filter(tag_id=i.id, user_id=user.pk)
            tag_data.append({i.id: i.tag_name,
                             "id": i.id,
                            "tag_name": i.tag_name,
                            "tag_articles": len(tag_articles)})
        return Response(tag_data, status=status.HTTP_200_OK)