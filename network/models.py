from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    followers = models.ManyToManyField("self", symmetrical=False)
    
    def serialize(self):
        return {
            "followers": self.followers
        }
    

class Post(models.Model):
    body = models.CharField(max_length=300)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    like = models.IntegerField(default=0)
    
    def serialize(self):
        return {
            "user": self.user,
            "body": self.body
        }
    