from django.shortcuts import render

from django.core.paginator import Paginator


from my_blog.models import Post, Tag

# Create your views here.


def posts_article(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    print(paginator.page_range)

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
    return render(request, 'network/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'network/tagsList.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'network/tagDetail.html', context={'tag': tag})


def index(request):
    return render(request, 'trands/trandsPage.html')
