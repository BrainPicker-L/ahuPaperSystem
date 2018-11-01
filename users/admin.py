from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_name', 'stu_id', 'major')