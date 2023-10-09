from django.db import models


class Comment(models.Model):
    user_id = models.ForeignKey('user.User', verbose_name='회원아이디', on_delete=models.CASCADE, related_name='comments')
    article_id = models.ForeignKey('articles.Article',  verbose_name='글 번호', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField('댓글')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)