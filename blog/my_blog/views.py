from django.shortcuts import render
from django.views import View

from .models import Post, Tag

# Create your views here.


def posts_article(request):
    posts = Post.objects.all()
    return render(request, 'network/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'network/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'network/tagsList.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'network/tagDetail.html', context={'tag': tag})


class post_update(View):
    def get(self, request, slug):
        tag = Tag.object.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'network/post_update.html', context={'form': bound_form, 'tag': tag})

