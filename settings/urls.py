"""ArxivApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from arxivapp.views import (
    category_list, article_list, article_detail, login_page,
    register, my_post_page, my_like_page, logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name="logout"),
    path('', register, name='register'),
    path('categories/', category_list, name='category'),
    path('articles/<category>', article_list, name='articles'),
    path('article/<id>', article_detail, name='article_detail'),
    path('mypostpage/', my_post_page, name='my_post_page'),
    path('mylikepage/', my_like_page, name='my_like_page')
]
