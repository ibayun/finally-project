from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_article),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tags_detail_url')
]
