from django import template
from django.urls import resolve, reverse
from django.db.models import Q
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    current_url = resolve(request.path_info).url_name
    menu_items = MenuItem.objects.filter(Q(parent__isnull=True) & Q(name=menu_name))
    return {'menu_items': menu_items, 'current_url': current_url}

@register.filter(name='is_current')
def is_current(url, current_url):
    return url == current_url or url == reverse(current_url)
