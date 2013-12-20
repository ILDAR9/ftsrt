# -*- coding: utf-8 -*-
from django.template import Library

register = Library()

def get_city(obj):
    dict_city = dict((x, y) for x, y in obj.choice_city)
    return dict_city.get(obj.city).encode('utf8')

def get_address(obj):
    return obj.address.encode('utf8')

@register.simple_tag
def map_url(obj):
    return "http://maps.yandex.ru/?text=город %s,%s" % (get_city(obj), get_address(obj))

@register.simple_tag
def stsr_url(obj):
    return "http://db.rusdsu.ru/index.php?id=0&what=Search&book_no=%d" % obj.stsr_id

@register.simple_tag
def club_city(obj):
    return get_city(obj)