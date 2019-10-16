from django.contrib import admin

from my_blog.models import Post

from my_blog.models import Tag

from my_blog.models import Comments

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)

# Register your models here.
