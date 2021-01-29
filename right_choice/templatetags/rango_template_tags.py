from django import template
from rango.models import University

register = template.Library()

@register.inclusion_tag('rango/university.html')
def get_university_list():
    return {'university': University.objects.all()}