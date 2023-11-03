from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    scheduled_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

