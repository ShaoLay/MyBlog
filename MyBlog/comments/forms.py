#!/usr/bin/env python
# encoding:utf8
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from comments.models import Comment


class CommentForm(ModelForm):
    url = forms.URLField(label='网址', required=False)
    if User.is_authenticated:
        email = forms.EmailField(label='电子邮箱', required=False, widget=forms.HiddenInput)
        name = forms.CharField(label='姓名', widget=forms.HiddenInput)
    else:
        email = forms.EmailField(label='电子邮箱', required=False)
        name = forms.CharField(label='姓名')
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)


    class Meta:
        model = Comment
        fields = ['body']