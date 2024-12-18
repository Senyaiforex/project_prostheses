import nested_admin
from django.contrib import admin
from .models import SpecialistModel, VideoModel, CategoryModel


@admin.register(SpecialistModel)
class TagAdmin(nested_admin.NestedModelAdmin):
    fields = ['full_name', 'job_title', 'bio', 'photo', 'image_tag', 'hidden']
    readonly_fields = ['image_tag']
    list_filter = ('hidden',)
    actions = ['deactivate_specialists']

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def deactivate_specialists(self, request, queryset):
        # Обновляем выбранные объекты, устанавливая active=False
        updated = queryset.update(hidden=True)
        self.message_user(request, f'{updated} специалистов скрыты.')

    deactivate_specialists.short_description = 'Скрыть выбранных специалистов'


@admin.register(CategoryModel)
class CategoryAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title',)

    class Meta:
        verbose_name = 'Категория видео'
        verbose_name_plural = 'Категории видео'


@admin.register(VideoModel)
class VideoAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('category__title',)
    fields = ['title', 'description', 'category', 'video', 'preview', 'slug', 'video_tag']
    readonly_fields = ['video_tag']
    ordering = ['-created_at', '-updated_at']

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео контент'
