from dis import CACHE

from django.shortcuts import render

from news.models import News, Category


# Create your views here.

def index(request):
    news = News.objects.order_by('-published_time')[0:5]
    latest_news = News.objects.order_by('-published_time')[0]
    latest_three_news = News.objects.order_by('-published_time')[1:4]
    context = {
        'news': news,
        'latest_news': latest_news,
        'latest_three_news': latest_three_news,
    }
    return render(request, 'index.html', context)


def categories_view(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'categori.html', context)


def category_detail(request, id):
    categories = Category.objects.all()
    news = News.objects.filter(category__id=id)
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'categori.html', context)

def nimadir(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news,
    }
    return render(request, 'nimadir.html', context)


def news_detail(request, slug):
    news = News.objects.get(slug=slug) # SELECT * FROM news WHERE slug = slug
    news.views_count += 1
    news.save()
    context = {
        'news': news,
    }
    return render(request, 'details.html', context)
