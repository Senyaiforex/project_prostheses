from django.contrib import admin
from .models import *
from django import forms

admin.AdminSite.site_header = 'Администрирование Море Протезов'

from django.contrib import admin
import nested_admin


class TextContentForm(forms.ModelForm):
    """
    Форма для текстового контента
    """

    class Meta:
        model = TextContent
        fields = '__all__'
        widgets = {
                'field_1': forms.Textarea(attrs={'rows': 8, 'style': 'width: 100%; resize: vertical;'}),
                'field_2': forms.Textarea(attrs={'rows': 8, 'style': 'width: 100%; resize: vertical;'}),
                'field_3': forms.Textarea(attrs={'rows': 8, 'style': 'width: 100%; resize: vertical;'}),
        }


class PlaceHolderInline(nested_admin.NestedTabularInline):
    model = PlaceHolder
    extra = 0
    fields = ['text']
    ordering = ('position',)

    def has_delete_permission(self, request, obj=None):
        return False


class FormInline(nested_admin.NestedTabularInline):
    model = FormContent
    extra = 0
    fields = ['title', 'button', 'accept']
    ordering = ('position',)
    inlines = [PlaceHolderInline]

    def has_delete_permission(self, request, obj=None):
        return False


class FieldContentInline(nested_admin.NestedTabularInline):
    model = FieldContent
    extra = 0
    fields = ('field_1', 'field_2', 'field_3', 'image', 'image_tag')
    # После разработки убрать position tag из fields
    readonly_fields = ('image_tag',)
    ordering = ('position',)
    form = TextContentForm

    def has_delete_permission(self, request, obj=None):
        return False


class ListRelatedContentInline(nested_admin.NestedTabularInline):
    model = ListRelatedContent
    extra = 0
    fields = ('description', 'tag_dev')
    # После разработки убрать position tag из fields
    ordering = ('position',)
    inlines = [FieldContentInline]

    def has_delete_permission(self, request, obj=None):
        return False


class TextContentInline(nested_admin.NestedTabularInline):
    model = TextContent
    extra = 0
    fields = ('title', 'data', 'tag_dev')
    # После разработки убрать position tag из fields
    ordering = ('position',)

    def has_delete_permission(self, request, obj=None):
        return False


class ImageContentInline(nested_admin.NestedTabularInline):
    model = ImageContent
    extra = 0
    fields = ('title', 'data', 'image_tag')
    # После разработки убрать position tag из fields
    readonly_fields = ('image_tag',)
    ordering = ('position',)

    def has_delete_permission(self, request, obj=None):
        return False


class HeaderContentInline(nested_admin.NestedTabularInline):
    model = HeaderContent
    extra = 0
    fields = ('title', 'type', 'data')
    # После разработки убрать position tag из fields
    ordering = ('position',)

    def has_delete_permission(self, request, obj=None):
        return False


class ButtonContentInline(nested_admin.NestedTabularInline):
    model = ButtonContent
    extra = 0
    fields = ('title', 'field_1', 'field_2', 'image', 'image_tag')
    readonly_fields = ('image_tag',)
    # После разработки убрать position tag из fields
    ordering = ('position',)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Page)
class MainPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(MainPageAdmin, self).get_queryset(request).filter(
                page='main'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutPage)
class AboutPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(AboutPageAdmin, self).get_queryset(request).filter(
                page='about'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HipPage)
class HipPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(HipPageAdmin, self).get_queryset(request).filter(
                page='hip'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(LegPage)
class LegPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(LegPageAdmin, self).get_queryset(request).filter(
                page='leg'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ArmPage)
class ArmPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(ArmPageAdmin, self).get_queryset(request).filter(
                page='arm'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SportPage)
class SportPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(SportPageAdmin, self).get_queryset(request).filter(
                page='sport'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SwimPage)
class SwimPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(SwimPageAdmin, self).get_queryset(request).filter(
                page='swim'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactPage)
class ContactPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(ContactPageAdmin, self).get_queryset(request).filter(
                page='contacts'
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FooterPage)
class FooterPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TextContentInline, HeaderContentInline, ImageContentInline, ButtonContentInline, FormInline,
               ListRelatedContentInline]
    list_display = ('title',)
    ordering = ('position',)
    fields = ('title', 'description')

    def get_queryset(self, request):
        return super(FooterPageAdmin, self).get_queryset(request).filter(
                page='footer'
        )

    def has_delete_permission(self, request, obj=None):
        return False
