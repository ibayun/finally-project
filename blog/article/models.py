from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time




"""class Tag(models.Model):
    tag_title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(int(time()))
        super().save(*args, **kwargs)

"""
