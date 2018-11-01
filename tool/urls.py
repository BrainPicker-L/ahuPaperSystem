from django.urls import path
from . import views
urlpatterns = [
    path('', views.paper_list, name='paper_list'),
    path('type/<int:paper_type_pk>', views.papers_with_type, name="papers_with_type"),
]