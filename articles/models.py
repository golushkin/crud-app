from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])



class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True
    )
    body = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.article.id)])
