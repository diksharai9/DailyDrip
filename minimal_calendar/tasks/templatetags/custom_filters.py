from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def completed_count(tasks):
    return len([t for t in tasks if t.completed])