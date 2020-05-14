from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    cuts all the values same as args
    """
    return value.replace(arg, '')
