from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .utils import ObjectUpdateMixin, ObjectCreateMixin, ObjectDeleteMixin

from .forms import TagForm, PostForm

from .models import Post, Tag

from django.core.paginator import Paginator


# def posts_article(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 4)
#     page = paginator.get_page(1)
#     return render(request, 'network/index.html', context={'posts': page.object_list})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'network/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'network/tagsList.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'network/tagDetail.html', context={'tag': tag})


def my_blog_list(request):
    search_question = request.GET.get('search', '')
    if search_question:
        posts = Post.objects.filter(
            Q(article_title__icontains=search_question) |
            Q(article_text__icontains=search_question)
        )



    else:
        posts = (Post.objects.filter(created_by_id=request.user.id))

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return render(request, 'network/index.html', context={
        'page_objects': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
    })


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'network/tagCreate.html'


class PostCreate(ObjectCreateMixin, CreateView, View):
    model_form = PostForm
    template = 'network/postCreate.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'network/postUpdate.html'


# class TagUpdate(ObjectUpdateMixin, View):
#     model = Tag
#     model_form = TagForm
#     template = 'network/tagUpdate.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'network/postDelete.html'
    redirect_url = 'post_list_url'


# class TagDelete(ObjectDeleteMixin, View):
#     model = Tag
#     template = 'network/tagDelete.html'
#     redirect_url = 'tags_list_url'
