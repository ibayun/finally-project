from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_article, name='post_list_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('create_tag', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete', TagDelete.as_view(), name='tag_delete_url'),



    path('create_article', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),

]
