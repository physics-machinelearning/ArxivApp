from django.shortcuts import render

from arxivapp.config import CATEGORIES


def category_list(request):
    context = {'categories': CATEGORIES.keys()}
    return render(request, 'category.html', context)
