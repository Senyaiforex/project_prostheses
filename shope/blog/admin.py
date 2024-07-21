from django.contrib import admin
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'tag')
    search_fields = ('title', 'sub_title', 'content')
    list_filter = ('tag',)
    fields = ['title', 'data', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
