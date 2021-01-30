import sys
import os
import django
from django.db.utils import IntegrityError

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
