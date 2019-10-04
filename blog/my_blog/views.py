from django.shortcuts import render
from .models import Post

# Create your views here.


def posts_article(request):
    posts = Post.objects.all()
    return render(request, 'network/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'network/post_detail.html', context={'post': post})
