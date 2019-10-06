from django.shortcuts import render, redirect
from django.views import View

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


class TagCreate(View):
    def get(self, request):
        form = TagForm
        return render(request, 'network/tagCreate.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'network/tagCreate.html', context={'form': bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'network/postCreate.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'network/postCreate.html', context={'form': bound_form})


class PostUpdate(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'network/postUpdate.html', context={'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            update_post = bound_form.save()
            return redirect(update_post)
        return render(request, 'network/postUpdate.html', context={'form': bound_form, 'post': post})


class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'network/tagUpdate.html', context={'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            update_tag = bound_form.save()
            return redirect(update_tag)
        return render(request, 'network/tagUpdate.html', context={'form': bound_form, 'tag': tag})
