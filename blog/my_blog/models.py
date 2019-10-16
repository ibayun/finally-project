from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from users.models import User
from django.db import models
from django.shortcuts import reverse
from time import time
from django.utils.text import slugify


def generate_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    created_by = models.ForeignKey(User, verbose_name="user", on_delete='CASCADE')
    article_title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    article_text = models.TextField(blank=True, db_index=True)
    article_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    picture = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name='image')
    comments = GenericRelation('comments')
    # likes = models.PositiveIntegerField(default=0)
    # dislikes = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.article_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.article_title

    class Meta:
        ordering = ['-article_date']


class Tag(models.Model):
    created_by = models.ForeignKey(User, verbose_name="user", on_delete='CASCADE')
    tag_title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    tag_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('tag_update_url', kwargs={'slug': self.slug})
    #
    # def get_delete_url(self):
    #     return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(int(time()))
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.tag_title)

    class Meta:
        ordering = ['-tag_date']


class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete='CASCADE')
    post = models.ForeignKey(Post, verbose_name='Заметка', on_delete='CASCADE')
    text = models.TextField()
    date_comments = models.DateTimeField(auto_now_add=True)

    # type_comments = models.ForeignKey(GenericForeignKey, on_delete='CASCADE')
    # id_comments = models.PositiveIntegerField()
    # content_comment = GenericForeignKey('type_comments', 'id_comments')
