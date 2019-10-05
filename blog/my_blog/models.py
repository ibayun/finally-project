from django.db import models
from django.shortcuts import reverse
from time import time
from django.utils.text import slugify


def generate_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):

    article_title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    article_text = models.TextField(blank=True, db_index=True)
    article_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.article_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.article_title


class Tag(models.Model):
    tag_title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.tag_title)
