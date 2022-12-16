from django.db import models
from main.models import Post
from account.models import User



class PostComment(models.Model):
    user_id = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

