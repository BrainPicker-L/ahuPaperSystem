from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import ClickRecord, ClickCount

register = template.Library()


@register.simple_tag
def get_click_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    click_count, created = ClickCount.objects.get_or_create(content_type=content_type, object_id=obj.pk)
    return click_count.click_num

@register.simple_tag
def get_content_type(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return content_type.model