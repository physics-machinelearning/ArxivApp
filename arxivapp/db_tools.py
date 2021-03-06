import sys
import os
import datetime

import django
from django.db.utils import IntegrityError
from django.db.models import Q

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

from arxivapp.models import Article, Post, UserArticle


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
        articles = Article.objects.filter(big_cat=category).order_by('published')
        articles = articles.all()
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


class InteractPost:
    def __init__(self, user):
        self.user = user

    def get_my_posts(self, article):
        posts = Post.objects.filter(
            article=article,
            user=self.user
        ).all()
        return posts

    def get_my_articles(self):
        posts = Post.objects.filter(
            user=self.user
        ).all()
        articles = [post.article for post in posts]
        i = 0
        while True:
            article = articles[i]
            if article in articles[:i]:
                articles.pop(i)
                i -= 1
            if i == len(articles)-1:
                break
            i += 1
        return articles

    def delete_post(self, count, article):
        posts = self.get_my_posts(article)
        post_id = posts[count].id
        post = Post.objects.get(id=post_id)
        post.delete()

    def get_other_posts(self, article):
        posts = Post.objects\
            .filter(article=article).exclude(user=self.user).all()
        return posts

    def get_post_instance(self, article):
        post_instance = Post(
            article=article,
            user=self.user
        )
        return post_instance
    
    def get_post_num(self, article):
        posts = Post.objects.filter(article=article)
        return len(posts)


class InteractUserArticle:
    def __init__(self, user):
        self.user = user

    def get_like(self, article):
        ua = UserArticle.objects.filter(
            article=article,
            user=self.user
        )
        if ua:
            return True
        else:
            return False

    def get_liked_articles(self):
        uas = UserArticle.objects.filter(
            user=self.user
        ).all()
        articles = [ua.article for ua in uas]
        return articles

    def like(self, article):
        ua = UserArticle(
            article=article,
            user=self.user
        )
        ua.save()

    def unlike(self, article):
        ua = UserArticle.objects.filter(
            article=article,
            user=self.user
        )
        ua.delete()
    
    def get_like_num(self, article):
        uas = UserArticle.objects.filter(
            article=article
        ).all()
        if uas:
            return len(uas)
        else:
            return 0
