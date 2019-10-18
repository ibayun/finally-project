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
        obj = self.model.objects.get(slug=slug)
        print(obj)
        obj.delete()
        return redirect(reverse(self.redirect_url))
