from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Tag
from user.models import User

from .serializers import TagSerializer


class TagView(APIView):
    def post(self, request):
        """ 목표를 직접 생성 """
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(pk=request.user.pk)
        user.tag_ids.add(serializer.data['id'])
        return Response({"message":"성공."}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        """ 이미 있는 목표를 설정 """
        user = User.objects.get(pk=request.user.pk)
        print(user)
        if user.tag_ids == pk:
            return Response({"message":"이미 설정된 목표입니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                tag = Tag.objects.get(pk=pk)
                user.tag_ids.add(tag)
            except ObjectDoesNotExist:
                return Response({"message":"존재하지 않는 태그입니다."}, status=status.HTTP_400_BAD_REQUEST)


            return Response({"message":"성공."}, status=status.HTTP_200_OK)