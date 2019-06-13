import hashlib
import urllib

from django import template
from django.conf import settings
import markdown2
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import random
from blog.models import Article, Category, Tag, Links
from django.utils.encoding import force_text

from comments.models import Comment

register = template.Library()


@register.simple_tag
def timeformat(data):
    try:
        return data.strftime(settings.TIME_FORMAT)
        # print(data.strftime(settings.TIME_FORMAT))
        # return "ddd"
    except:
        return ""


@register.simple_tag
def datetimeformat(data):
    try:
        return data.strftime(settings.DATE_TIME_FORMAT)
    except:
        return ""


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    return mark_safe(markdown2.markdown(force_text(content),
                                        extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables",
                                                "spoiler"]))
    """
    return mark_safe(markdown.markdown(content,
                                       extensions=
                                       ['markdown.extensions.fenced_code',
                                        'markdown.extensions.codehilite'],
                                       safe_mode=True, enable_attributes=False))
    """


@register.inclusion_tag('blog/tags/breadcrumb.html')
def load_breadcrumb(article):
    names = article.get_category_tree()

    names.append((settings.SITE_NAME, 'http://127.0.0.1:8000'))
    names = names[::-1]

    return {
        'names': names,
        'title': article.title
    }


@register.inclusion_tag('blog/tags/articletaglist.html')
def load_articletags(article):
    tags = article.tags.all()
    tags_list = []
    for tag in tags:
        url = tag.get_absolute_url()
        count = tag.get_article_count()
        tags_list.append((
            url, count, tag, random.choice(settings.BOOTSTRAP_COLOR_TYPES)
        ))
    return {
        'article_tags_list': tags_list
    }


@register.inclusion_tag('blog/tags/sidebar.html')
def load_sidebar():
    recent_articles = Article.objects.filter(status='p')[:settings.SIDEBAR_ARTICLE_COUNT]
    sidebar_categorys = Category.objects.all()
    most_read_articles = Article.objects.filter(status='p').order_by('-views')[:settings.SIDEBAR_ARTICLE_COUNT]
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    links = Links.objects.all()
    commment_list = Comment.objects.order_by('-id')[:settings.SIDEBAR_COMMENT_COUNT]

    # tags=
    return {
        'recent_articles': recent_articles,
        'sidebar_categorys': sidebar_categorys,
        'most_read_articles': most_read_articles,
        'article_dates': dates,
        'sidabar_links': links,
        'sidebar_comments': commment_list
    }


@register.inclusion_tag('blog/tags/article_meta_info.html')
def load_article_metas(article):
    return {
        'article': article
    }


@register.inclusion_tag('blog/tags/article_info.html')
def load_article_detail(article, isindex):
    return {
        'article': article,
        'isindex': isindex
    }

@register.filter
def gravatar_url(email, size=40):
    email = email.encode('utf-8')
    default = "https://avatar.duoshuo.com/avatar-50/928/120117.jpg".encode('utf-8')
    return "https://www.gravatar.com/avatar/%s?%s" % (
        hashlib.md5(email.lower()).hexdigest(), urllib.parse.urlencode({'d': default, 's': str(size)}))

@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))
