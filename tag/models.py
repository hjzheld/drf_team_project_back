from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)