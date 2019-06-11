from django import template
from django.conf import settings
import datetime


register = template.Library()


@register.simple_tag
def timeformat(data):
    try:

        print(data.strftime(settings.TIME_FORMAT))
        return "ddd"
    except:
        return "111"