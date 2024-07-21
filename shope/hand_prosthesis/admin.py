from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = HandTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = HandImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = HandHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = HandButtonContent


@admin.register(HandSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
