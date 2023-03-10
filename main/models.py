from django.db import models

from account.models import User

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username}-> {self.body}'
