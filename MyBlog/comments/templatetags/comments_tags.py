#!/usr/bin/env python
# encoding: utf-8
from django import template
from django.template.loader import render_to_string
from ..models import Comment
from blog.models import Article

register = template.Library()


@register.simple_tag(name='get_comment_count')
def GetCommentCount(parser, token):
    #pkid = token
    #comments = Comment.objects
    return 'wergwergwergwerger'
