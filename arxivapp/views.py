from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from arxivapp.config import CATEGORIES
from arxivapp.db_tools import InteractArticle
from arxivapp.forms import ArticleSearchForm


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('category')
        else:
            return render(request, 'login.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password')
        if email and password and confirm_password:
            if password == confirm_password:
                user = authenticate(username=email, password=password)
                if user is None:
                    user = User.objects.create_user(
                        username=email,
                        password=password
                    )
                    user.save()
                    return redirect('login')
                else:
                    return redirect('login')
            else:
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')


def category_list(request):
    context = {'categories': CATEGORIES.keys()}
    return render(request, 'category.html', context)


def article_list(request, category):
    num = 10
    if request.method == 'GET':
        form = ArticleSearchForm()
        ia = InteractArticle()
        queryset = ia.get_articles(category)
        paginator = Paginator(queryset, num)
        page_int = request.GET.get('page', 1)
        page = paginator.get_page(page_int)
        context = {
            'form': form,
            'articles': page
            }
        return render(request, 'articles.html', context)
    elif request.method == 'POST':
        form = ArticleSearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            author = form.cleaned_data['author']
            ia = InteractArticle()
            articles = ia.search_articles(
                keyword, start_year, end_year, author
            )
            for article in articles:
                article['published'] = str(article['published'])
            request.session['queryset'] = articles
            paginator = Paginator(articles, num)
            page_int = 1
            page = paginator.get_page(page_int)
            context = {
                'form': form,
                'articles': page
            }
            return render(request, 'articles.html', context)


def article_detail(request, id):
    if request.method == 'GET':
        ia = InteractArticle()
        article = ia.get_article(id)
        context = {
            'article': article
        }
        return render(request, 'article_detail.html', context)