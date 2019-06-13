from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^article/(?P<article_id>\d+)/postcomment$', views.CommentPostView.as_view(), name='postcomment'),
]