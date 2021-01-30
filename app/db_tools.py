from .models import Article

class InteractArticle:
    def __init__(self):
        self.articles = []

    def insert_article(
        title, author, arxiv_url, summary, published, category
        ):
        article = Article(
            title, author, arxiv_url, summary, published, category
        )
        self.articles.append(article)
    
    def save_article(self):
        Article.objects.bulk_create(self.articles)
