import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import *

'''def get_today_hot_data(content_typr):
    today = timezone.now().date()
    date_filter = ClickRecord.objects.filter(content_typr=content_typr, )'''