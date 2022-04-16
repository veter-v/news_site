from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    context = {'news': news,
               'title': 'List of News'
               }
    return render(request, 'news/index.html', context)
