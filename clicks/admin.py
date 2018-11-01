from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ClickRecord)
class ClickRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'user', 'clicked_time',)

@admin.register(ClickCount)
class ClickCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'click_num',)