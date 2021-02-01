import sys
import os
import datetime

import django
from django.db.utils import IntegrityError
from django.db.models import Q

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

from arxivapp.models import Article


class InteractArticle:
    def __init__(self):
        self.articles = []

    def insert_article(
        self, title, author, arxiv_url, summary, published, category,
        big_cat
        ):
        article = Article(
            title=title,
            author=author,
            arxiv_url=arxiv_url,
            summary=summary,
            published=published,
            category=category,
            big_cat=big_cat
        )
        self.articles.append(article)
    
    def save_article(self):
        try:
            Article.objects.bulk_create(self.articles)
        except IntegrityError:
            for article in self.articles:
                try:
                    article.save()
                except IntegrityError:
                    pass

    def get_article_num(self):
        return len(Article.objects.all())

    def get_article(self, id):
        article = Article.objects.get(id=id)
        return article

    def get_articles(self, category):
        articles = Article.objects.filter(big_cat=category).all()
        return articles

    def search_articles(self, keyword, start, end, author):
        if keyword:
            articles = Article.objects.filter(
                Q(title__contains=keyword) |
                Q(summary__contains=keyword)
            )
        else:
            articles = Article.objects.filter()
        if start:
            start = datetime.datetime(
                year=int(start), month=1, day=1
                )
            articles = articles.filter(published__gte=start)
        if end:
            end = datetime.datetime(
                year=int(end)+1, month=1, day=1
                )
            articles = articles.filter(published__lte=end)
        if author:
            articles = articles.filter(author__contains=author)
        articles = articles.all().order_by('published').distinct()
        articles = articles.values()
        articles = list(articles)
        return articles
