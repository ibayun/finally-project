from django.shortcuts import render, redirect

from django.core.paginator import Paginator


from my_blog.models import Post, Tag
from django.db.models import Q
# Create your views here.
from my_blog.forms import CommentForm
from my_blog.models import Comments


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


def index(request):
    return render(request, 'trands/trandsPage.html')


# def delete(ObjectDeleteMixin, View):
#     model = Post
#     emplate = 'network/commentDelete.html'
#     redirect_url = 'http://127.0.0.1:8000/trands/post/wdsasdasd-1571164915'
    # class PostDelete(ObjectDeleteMixin, View):
    #     model = Post
    #     template = 'network/postDelete.html'
    #     redirect_url = 'post_list_url'