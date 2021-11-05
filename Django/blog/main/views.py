import math
from django.shortcuts import render
from article.models import Article
from math import ceil

def index(request, page=1):
    articles_in_page = 2
    offset = articles_in_page * (page - 1)
    articles = Article.objects.all() 
    article_count = articles.count()
    pages_range = range(1, int(math.ceil(article_count/ articles_in_page)+1))
    return render(request, 'index.html', {'articles': articles[offset : articles_in_page * page],
    'article_count': article_count, 'pages_range':pages_range})
