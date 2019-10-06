from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.Form):
    tag_title = forms.CharField(max_length=40)
    slug = forms.SlugField(max_length=40)


    """class Meta:
        model = Tag
        fields = [
            'tag_title',
            'slug'
        ]
        widgets = {
            'tag_title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})

        }"""

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug "{}" - was create.'.format(new_slug))

    def save(self):
        new_tag = Tag.objects.create(
            tag_title=self.cleaned_data['tag_title'],
            slug=self.cleaned_data['slug']
        )
        return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'article_title',
            'slug',
            'article_text',
            'tags',
        ]

        widgets = {
            'article_title': forms.TextInput(attrs={'class:' 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'article_text' : forms.Textarea(attrs={'class': 'form-control'}),
            'tags' : forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower();

        if new_slug == 'creatw':
                raise ValidationError('wrong name for "Slug"')
        return new_slug