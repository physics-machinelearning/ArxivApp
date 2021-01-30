from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length=1000)

    author = models.CharField(max_length=200)

    arxiv_url = models.CharField(max_length=1000)

    summary = models.CharField(max_length=1000)

    published = models.DateField()

    category = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
            name='unique_article')
        ]


class UserArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['article', 'user'],
                name='unique_userarticle'
                )
        ]


class Category(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['article', 'name'],
                name='unique_category'
                )
        ]