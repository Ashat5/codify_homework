from django.db import models
from article.models import Article

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    class Meta:
        ordering = ('-created_date',)
