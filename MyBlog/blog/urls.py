#!/usr/bin/env python
# encoding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_name>\w+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^author/(?P<author_name>\w+)$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^tags/(?P<tag_name>\w+)$', views.TagDetailView.as_view(), name='tag_detail'),
    url(r'(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<article_id>\d+)-(?P<slug>\S+).html$',views.ArticleDetailView.as_view(),name='detail'),
]
