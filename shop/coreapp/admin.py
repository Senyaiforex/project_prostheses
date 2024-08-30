import nested_admin
from django.contrib import admin
from .models import SpecialistModel, VideoModel, CategoryModel


@admin.register(SpecialistModel)
class TagAdmin(nested_admin.NestedModelAdmin):
    fields = ['full_name', 'job_title', 'bio', 'photo', 'image_tag']
    readonly_fields = ['image_tag']

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


@admin.register(CategoryModel)
class CategoryAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title',)

    class Meta:
        verbose_name = 'Категория видео'
        verbose_name_plural = 'Категории видео'


@admin.register(VideoModel)
class VideoAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('category__title',)
    fields = ['title', 'description', 'category', 'video', 'preview', 'slug', 'video_tag']
    readonly_fields = ['video_tag', 'slug']

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео контент'
