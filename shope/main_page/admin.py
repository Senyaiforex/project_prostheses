from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(TextMixin, admin.TabularInline):
    model = MainTextContent


class ImageContentInline(ImageMixin, admin.TabularInline):
    model = MainImageContent


class HeaderContentInline(HeaderMixin, admin.TabularInline):
    model = MainHeaderContent


class ButtonContentInline(ButtonMixin, admin.TabularInline):
    model = MainButtonContent


@admin.register(MainSection)
class SectionAdmin(SectionMixin, admin.ModelAdmin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
