import nested_admin
from django.contrib import admin
from .models import Tag, Blog

from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Blog


class CommentForm(forms.ModelForm):
    """Form for comments to the article."""

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
                "text": CKEditor5Widget(
                        attrs={"class": "django_ckeditor_5"}, config_name="extends"
                )
        }


@admin.register(Tag)
class TagAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


@admin.register(Blog)
class BlogAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'sub_title', 'tag')
    search_fields = ('title', 'sub_title', 'content')
    list_filter = ('tag',)
    fields = ['title', 'sub_title', 'content', 'tag', 'image', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
