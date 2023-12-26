from django import template
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_image_url(image_field):
    if image_field and hasattr(image_field, 'url'):
        return image_field.url
    return static('img/default/no-image.png')