from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Post(models.Model):
    objects = None
    article_title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    article_text = models.TextField(blank=True, db_index=True)
    article_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.article_title
