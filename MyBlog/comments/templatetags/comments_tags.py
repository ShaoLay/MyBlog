#!/usr/bin/env python
# encoding: utf-8
from django import template
from django.template.loader import render_to_string
from ..models import Comment
from blog.models import Article

register = template.Library()


@register.simple_tag(name='get_comment_count')
def GetCommentCount(parser, token):
    commentcount = Comment.objects.filter(article__author_id=token).count()
    return "0" if commentcount == 0 else str(commentcount) + " comments"

