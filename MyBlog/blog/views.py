from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
import markdown2

from blog.models import Article, Category


class IndexView(ListView):

    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body)
        return article_list

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)