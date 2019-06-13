from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from .models import *
from django import forms


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Links)
