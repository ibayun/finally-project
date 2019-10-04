from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_article),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
]
