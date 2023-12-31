from django.db import models
from user.models import User
from tag.models import Tag



# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='uploads/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="like_articles", blank=True)
    
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)