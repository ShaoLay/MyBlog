from . models import Category, Article, Tag
from django.conf import settings


def seo_processor(requests):
    return {
        'SITE_NAME':settings.SITE_NAME,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
        'SITE_BASE_URL': 'http://' + requests.get_host() + '/',
    }