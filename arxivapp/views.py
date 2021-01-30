from django.shortcuts import render

from arxivapp.config import CATEGORIES
from arxivapp.db_tools import InteractArticle


def category_list(request):
    context = {'categories': CATEGORIES.keys()}
    return render(request, 'category.html', context)


def article_list(request, category):
    ia = InteractArticle()
    articles = ia.get_articles(cateogry)
    context = {'articles': articles}
    return render(request, 'articles.html', context)
