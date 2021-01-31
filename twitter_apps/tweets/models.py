from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # сортировка, новые будут сверху
        ordering = ('-created_at',)
