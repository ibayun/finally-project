from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'tag_title',
        ]
        widgets = {
            'tag_title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug "{}" - was create.'.format(new_slug))


class PostForm(LoginRequiredMixin, forms.ModelForm, CreateView):
    class Meta:
        model = Post
        fields = [
            'article_title',
            'article_text',
            'tags',
            'picture',
        ]

        widgets = {
            'article_title': forms.TextInput(attrs={'class': 'form-control', 'size': 14, 'title': 'Enter your title'}),
            'article_text': forms.Textarea(attrs={'class': 'form-control', 'size': 14, 'title': 'Enter body post'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'title': 'choice tag'}),
        }

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('wrong name for "Slug"')
        return new_slug
