from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from my_blog.views import PostCreate
from .views import *

urlpatterns = [
    path('', posts_article, name='post_list_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),

    path('create_article', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    # path('post/<str:slug>/?id=<int:id>', delete, name='comment_delete_url'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
