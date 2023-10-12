from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"

    def get_nickname(self, obj):
        return obj.user_id.nickname
