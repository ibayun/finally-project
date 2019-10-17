from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from my_blog import views
from .views import *

urlpatterns = [
    path('myblog/', my_blog_list, name='my_blog_url'),

    path('trends/', posts_article, name='post_list_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('create_tag', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),




    path('create_article', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('post/<str:slug>/<int:id>', views.delete_comment, name='delete_comment')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

