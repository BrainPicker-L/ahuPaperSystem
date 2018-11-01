from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name',)

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'chinese_title', 'paper_type', 'author', 'publisher', 'ISSN', 'publish_year', 'keywords', 'paper_url',)


