from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.http import HttpResponseNotFound

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .utils import ObjectUpdateMixin, ObjectCreateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, CommentForm

from .models import Post, Tag, Comments

from django.core.paginator import Paginator


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    comment = Comments.objects.filter(post_id=post)
    # form = CommentForm(request.POST)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
            return redirect('post_detail_url', slug)

    else:
        form = CommentForm()
    return render(request, 'network/post_detail.html', context={
        'post': post,
        "comments": comment,
        "form": form,
    })


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
            Q(article_text__icontains=search_question),
            Q(created_by_id=request.user.id)
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


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'network/postDelete.html'
    redirect_url = 'post_list_url'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'network/tagDelete.html'
    redirect_url = 'tags_list_url'


def posts_article(request):
    search_question = request.GET.get('search', '')
    if search_question:
        posts = Post.objects.filter(
            Q(article_title__icontains=search_question) |
            Q(article_text__icontains=search_question)
        )
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 8)
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


def delete_comment(request, id, slug):
    try:

        comment = Comments.objects.get(id=id)
        comment.delete()
        return redirect('post_detail_url', slug)
    except Comments.DoesNotExist:
        return HttpResponseNotFound("<h2> Комментарий уже был удален. Вернитесь и обновите страницу. </h2>")