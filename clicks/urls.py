from django.urls import path
from . import views


urlpatterns = [
    path('click_change', views.click_change, name='click_change')
]