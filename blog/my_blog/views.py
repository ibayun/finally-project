from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .utils import ObjectUpdateMixin, ObjectCreateMixin, ObjectDeleteMixin

from .forms import TagForm, PostForm

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


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'network/tagCreate.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'network/postCreate.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'network/postUpdate.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'network/tagUpdate.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'network/postDelete.html'
    redirect_url = 'post_list_url'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'network/tagDelete.html'
    redirect_url = 'tags_list_url'

