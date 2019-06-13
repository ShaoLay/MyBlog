#!/usr/bin/env python
# encoding: utf-8
from .models import Comment
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class CommentForm(ModelForm):
    url = forms.URLField(label='网址', required=False)
    email = forms.EmailField(label='电子邮箱', required=False)
    name = forms.CharField(label='姓名')
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['body']
