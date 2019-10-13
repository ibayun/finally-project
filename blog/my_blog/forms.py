from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Tag, Post


class TagForm(forms.ModelForm):
    """tag_title = forms.CharField(max_length=40)
    #slug = forms.SlugField(max_length=40)"""

    class Meta:
        model = Tag
        fields = [
            'tag_title',
            #'slug'
        ]
        widgets = {
            'tag_title': forms.TextInput(attrs={'class': 'form-control'}),
            #'slug': forms.TextInput(attrs={'class': 'form-control'})

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug "{}" - was create.'.format(new_slug))

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         tag_title=self.cleaned_data['tag_title'],
    #         #slug=self.cleaned_data['slug']
    #     )
    #     return new_tag


class PostForm(forms.ModelForm, LoginRequiredMixin, CreateView):
    class Meta:
        model = Post
        fields = [
            'article_title',
            # 'slug',
            'article_text',
            'tags',
        ]

        widgets = {
            'article_title': forms.TextInput(attrs={'class': 'form-control', 'size': 14, 'title': 'Enter your title'}),
            #   'slug': forms.TextInput(attrs={'class': 'form-control', 'size': 14, 'title': 'Enter your slug'}),
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



