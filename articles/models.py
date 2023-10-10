from django.db import models
from user.models import User
from tag.models import Tag



# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

def __str__(self):
    return str(self.title)