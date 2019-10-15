from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


class ObjectCreateMixin(LoginRequiredMixin, CreateView):
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        print(self.request)
        return render(request, self.template, context={'form': form})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def post(self, request):
        bound_form = self.model_form(request.POST, request.FILES)
        print(bound_form)
        if bound_form.is_valid():
            self.object = bound_form.save(commit=False)
            self.object.created_by = self.request.user
            self.object.save()
            print(self.object)
            return redirect(self.object)

        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        print(bound_form)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        print(bound_form)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request,  self.template, context={self.model.__name__.lower: obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))


# class ObjectPostListMixin:
#     model = None
#     template = None
#
#     def get(self, request):
#         search_question = request.GET.get('search', '')
#         if search_question:
#             posts = Post.objects.filter(
#                 Q(article_title__icontains=search_question) |
#                 Q(article_text__icontains=search_question),
#                 Q(created_by_id=request.user.id)
#             )
#
#         else:
#             posts = (Post.objects.filter(created_by_id=request.user.id))
#
#         paginator = Paginator(posts, 2)
#         page_number = request.GET.get('page', 1)
#         page = paginator.get_page(page_number)
#         is_paginated = page.has_other_pages()
#
#         if page.has_previous():
#             previous_url = '?page={}'.format(page.previous_page_number())
#         else:
#             previous_url = ''
#
#         if page.has_next():
#             next_url = '?page={}'.format(page.next_page_number())
#         else:
#             next_url = ''
#
#         return render(request, 'network/index.html', context={
#             'page_objects': page,
#             'is_paginated': is_paginated,
#             'next_url': next_url,
#             'previous_url': previous_url,
#         })
#
