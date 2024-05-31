from django.db import models
from django.contrib.auth.models import User
from .post import Post

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    likes: models.IntegerField(default=0)
    shares: models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.content