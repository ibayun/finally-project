from django.contrib import admin

from my_blog.models import Post

from my_blog.models import Tag

admin.site.register(Post)
admin.site.register(Tag)
# Register your models here.
