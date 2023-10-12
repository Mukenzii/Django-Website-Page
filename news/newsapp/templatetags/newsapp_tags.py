from django import template
from ..models import ArticleCategory
register = template.Library()

@register.simple_tag()
def get_categories():
    categories = ArticleCategory.objects.all()
    return categories