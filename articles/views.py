from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.

def index(request):
    article_list = Article.objects.order_by('-date')
    context = {'article_list': article_list}
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    article = Article.objects.get(pk = article_id)
    article.count = article.count+1
    article.save()
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
