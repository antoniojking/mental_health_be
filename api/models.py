from django.conf import settings
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 30, unique=True, error_messages={
        'unique': 'Name is already taken'
    })
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    body = models.CharField(max_length = 1000)
    upvote = models.IntegerField(default = 0)
    downvote = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'belongs to: ' + self.user.username + ' title: ' + self.title + ' body: ' + self.body
